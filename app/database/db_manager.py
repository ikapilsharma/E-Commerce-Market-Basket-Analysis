import pandas as pd
import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:
    def __init__(self):
        # Using your existing PostgreSQL database configuration
        self.connection_params = {
            'host': os.getenv('DB_HOST', 'localhost'),
            'database': os.getenv('DB_NAME', 'mba_db'),
            'user': os.getenv('DB_USER', 'matth'),
            'password': os.getenv('DB_PASSWORD', 'Delaune.7467'),
            'port': os.getenv('DB_PORT', '5432')
        }
        
    def get_connection(self):
        """Get database connection"""
        try:
            conn = psycopg2.connect(**self.connection_params)
            return conn
        except Exception as e:
            print(f"Database connection error: {e}")
            return None
    
    def execute_query(self, query, params=None):
        """Execute query and return DataFrame"""
        try:
            conn = self.get_connection()
            if conn is None:
                return pd.DataFrame()
            
            df = pd.read_sql_query(query, conn, params=params)
            conn.close()
            return df
            
        except Exception as e:
            print(f"Query execution error: {e}")
            return pd.DataFrame()
    
    def get_overall_stats(self):
        """Get overall statistics"""
        try:
            stats = {}
            
            # Total orders
            query = "SELECT COUNT(*) as total_orders FROM amazon_orders"
            result = self.execute_query(query)
            stats['total_orders'] = int(result['total_orders'].iloc[0]) if not result.empty else 0
            
            # Total revenue
            query = "SELECT SUM(amount) as total_revenue FROM amazon_order_items"
            result = self.execute_query(query)
            stats['total_revenue'] = float(result['total_revenue'].iloc[0]) if not result.empty else 0
            
            # Total products
            query = "SELECT COUNT(*) as total_products FROM amazon_products"
            result = self.execute_query(query)
            stats['total_products'] = int(result['total_products'].iloc[0]) if not result.empty else 0
            
            # Average order value
            query = """
            SELECT AVG(order_total) as avg_order_value 
            FROM (
                SELECT order_id, SUM(amount) as order_total 
                FROM amazon_order_items 
                GROUP BY order_id
            ) order_totals
            """
            result = self.execute_query(query)
            stats['avg_order_value'] = float(result['avg_order_value'].iloc[0]) if not result.empty else 0
            
            # Date range
            query = "SELECT MIN(date) as start_date, MAX(date) as end_date FROM amazon_orders"
            result = self.execute_query(query)
            if not result.empty:
                stats['date_range'] = {
                    'start_date': result['start_date'].iloc[0].strftime('%Y-%m-%d'),
                    'end_date': result['end_date'].iloc[0].strftime('%Y-%m-%d')
                }
            
            return stats
            
        except Exception as e:
            return {"error": str(e)}
    
    def get_top_products(self, limit=20):
        """Get top performing products"""
        try:
            query = """
            SELECT 
                ap.product_name,
                ap.category,
                COUNT(aoi.order_id) as order_count,
                SUM(aoi.qty) as total_quantity,
                SUM(aoi.amount) as total_revenue,
                AVG(aoi.amount) as avg_price
            FROM amazon_order_items aoi
            JOIN amazon_products ap ON aoi.sku = ap.sku
            WHERE ap.product_name IS NOT NULL
            GROUP BY ap.product_name, ap.category
            ORDER BY total_revenue DESC
            LIMIT %s
            """
            
            result = self.execute_query(query, (limit,))
            if result.empty:
                return []
            
            # Convert to JSON-serializable format
            products_list = []
            for _, row in result.iterrows():
                products_list.append({
                    "product_name": str(row['product_name']),
                    "category": str(row['category']),
                    "order_count": int(row['order_count']),
                    "total_quantity": int(row['total_quantity']),
                    "total_revenue": float(row['total_revenue']),
                    "avg_price": float(row['avg_price'])
                })
            
            return products_list
            
        except Exception as e:
            return {"error": str(e)}
    
    def get_sales_trends(self):
        """Get sales trends over time"""
        try:
            query = """
            SELECT 
                DATE_TRUNC('month', ao.date) as month,
                COUNT(DISTINCT ao.order_id) as orders,
                SUM(aoi.amount) as revenue,
                AVG(aoi.amount) as avg_order_value
            FROM amazon_orders ao
            JOIN amazon_order_items aoi ON ao.order_id = aoi.order_id
            GROUP BY DATE_TRUNC('month', ao.date)
            ORDER BY month
            """
            
            result = self.execute_query(query)
            if result.empty:
                return []
            
            # Convert to JSON-serializable format
            trends_list = []
            for _, row in result.iterrows():
                trends_list.append({
                    "month": row['month'].strftime('%Y-%m'),
                    "orders": int(row['orders']),
                    "revenue": float(row['revenue']),
                    "avg_order_value": float(row['avg_order_value'])
                })
            
            return trends_list
            
        except Exception as e:
            return {"error": str(e)}
    
    def get_category_performance(self):
        """Get performance by category"""
        try:
            query = """
            SELECT 
                ap.category,
                COUNT(DISTINCT aoi.order_id) as orders,
                SUM(aoi.qty) as quantity,
                SUM(aoi.amount) as revenue,
                AVG(aoi.amount) as avg_price
            FROM amazon_order_items aoi
            JOIN amazon_products ap ON aoi.sku = ap.sku
            WHERE ap.category IS NOT NULL
            GROUP BY ap.category
            ORDER BY revenue DESC
            """
            
            result = self.execute_query(query)
            if result.empty:
                return []
            
            # Convert to JSON-serializable format
            categories_list = []
            for _, row in result.iterrows():
                categories_list.append({
                    "category": str(row['category']),
                    "orders": int(row['orders']),
                    "quantity": int(row['quantity']),
                    "revenue": float(row['revenue']),
                    "avg_price": float(row['avg_price'])
                })
            
            return categories_list
            
        except Exception as e:
            return {"error": str(e)}
    
    def get_geographic_distribution(self):
        """Get sales by geographic region"""
        try:
            query = """
            SELECT 
                ao.ship_state,
                ao.ship_country,
                COUNT(DISTINCT ao.order_id) as orders,
                SUM(aoi.amount) as revenue
            FROM amazon_orders ao
            JOIN amazon_order_items aoi ON ao.order_id = aoi.order_id
            WHERE ao.ship_state IS NOT NULL
            GROUP BY ao.ship_state, ao.ship_country
            ORDER BY revenue DESC
            LIMIT 50
            """
            
            result = self.execute_query(query)
            return result.to_dict('records') if not result.empty else []
            
        except Exception as e:
            return {"error": str(e)}
    
    def get_customer_metrics(self):
        """Get customer-related metrics"""
        try:
            query = """
            SELECT 
                COUNT(DISTINCT ao.ship_postal_code) as unique_customers,
                AVG(customer_orders.order_count) as avg_orders_per_customer,
                AVG(customer_orders.total_spent) as avg_customer_value
            FROM amazon_orders ao
            JOIN (
                SELECT 
                    ship_postal_code,
                    COUNT(*) as order_count,
                    SUM(aoi.amount) as total_spent
                FROM amazon_orders ao2
                JOIN amazon_order_items aoi ON ao2.order_id = aoi.order_id
                GROUP BY ship_postal_code
            ) customer_orders ON ao.ship_postal_code = customer_orders.ship_postal_code
            WHERE ao.ship_postal_code IS NOT NULL
            """
            
            result = self.execute_query(query)
            if result.empty:
                return {}
            
            return {
                'unique_customers': int(result['unique_customers'].iloc[0]),
                'avg_orders_per_customer': float(result['avg_orders_per_customer'].iloc[0]),
                'avg_customer_value': float(result['avg_customer_value'].iloc[0])
            }
            
        except Exception as e:
            return {"error": str(e)}
    
    def test_connection(self):
        """Test database connection"""
        try:
            conn = self.get_connection()
            if conn:
                conn.close()
                return {"status": "Connected", "message": "Database connection successful"}
            else:
                return {"status": "Failed", "message": "Could not connect to database"}
        except Exception as e:
            return {"status": "Error", "message": str(e)}
