import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
from database.db_manager import DatabaseManager
import json

class MarketBasketAnalyzer:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.transactions = None
        self.frequent_itemsets = None
        self.rules = None
        
    def prepare_transaction_data(self):
        """Prepare transaction data for Apriori algorithm"""
        try:
            # Get order items grouped by order_id
            query = """
            SELECT 
                ao.order_id,
                ap.product_name,
                aoi.qty
            FROM amazon_orders ao
            JOIN amazon_order_items aoi ON ao.order_id = aoi.order_id
            JOIN amazon_products ap ON aoi.sku = ap.sku
            WHERE ap.product_name IS NOT NULL
            ORDER BY ao.order_id
            """
            
            df = self.db_manager.execute_query(query)
            
            # Create transaction list
            transactions = []
            for order_id in df['order_id'].unique():
                order_items = df[df['order_id'] == order_id]['product_name'].tolist()
                if len(order_items) > 1:  # Only include orders with multiple items
                    transactions.append(order_items)
            
            # Convert to transaction format for Apriori
            te = TransactionEncoder()
            te_ary = te.fit(transactions).transform(transactions)
            self.transactions = pd.DataFrame(te_ary, columns=te.columns_)
            
            return True
        except Exception as e:
            print(f"Error preparing transaction data: {e}")
            return False
    
    def analyze(self, min_support=0.01, min_confidence=0.3):
        """Perform market basket analysis using Apriori algorithm"""
        try:
            if self.transactions is None:
                if not self.prepare_transaction_data():
                    return {"error": "Failed to prepare transaction data"}
            
            # Find frequent itemsets using Apriori
            self.frequent_itemsets = apriori(
                self.transactions, 
                min_support=min_support, 
                use_colnames=True
            )
            
            if self.frequent_itemsets.empty:
                return {"error": "No frequent itemsets found with given support"}
            
            # Generate association rules
            self.rules = association_rules(
                self.frequent_itemsets, 
                metric="confidence", 
                min_threshold=min_confidence
            )
            
            # Prepare results with JSON-serializable data
            frequent_itemsets_list = []
            for _, row in self.frequent_itemsets.iterrows():
                frequent_itemsets_list.append({
                    "support": float(row['support']),
                    "itemsets": list(row['itemsets'])
                })
            
            association_rules_list = []
            for _, row in self.rules.iterrows():
                association_rules_list.append({
                    "antecedents": list(row['antecedents']),
                    "consequents": list(row['consequents']),
                    "support": float(row['support']),
                    "confidence": float(row['confidence']),
                    "lift": float(row['lift'])
                })
            
            results = {
                "frequent_itemsets": frequent_itemsets_list,
                "association_rules": association_rules_list,
                "summary": {
                    "total_transactions": int(len(self.transactions)),
                    "frequent_itemsets_count": int(len(self.frequent_itemsets)),
                    "association_rules_count": int(len(self.rules))
                }
            }
            
            return results
            
        except Exception as e:
            return {"error": f"Analysis failed: {str(e)}"}
    
    def get_top_associations(self, limit=20):
        """Get top association rules by lift"""
        if self.rules is None:
            return {"error": "No rules found. Run analysis first."}
        
        top_rules = self.rules.nlargest(limit, 'lift')
        top_associations_list = []
        for _, row in top_rules.iterrows():
            top_associations_list.append({
                "antecedents": list(row['antecedents']),
                "consequents": list(row['consequents']),
                "support": float(row['support']),
                "confidence": float(row['confidence']),
                "lift": float(row['lift'])
            })
        return {
            "top_associations": top_associations_list
        }
    
    def get_product_recommendations(self, product_name, limit=10):
        """Get product recommendations based on association rules"""
        if self.rules is None:
            return {"error": "No rules found. Run analysis first."}
        
        # Find rules where the product is in antecedents
        recommendations = self.rules[
            self.rules['antecedents'].apply(lambda x: product_name in str(x))
        ].nlargest(limit, 'confidence')
        
        recommendations_list = []
        for _, row in recommendations.iterrows():
            recommendations_list.append({
                "antecedents": list(row['antecedents']),
                "consequents": list(row['consequents']),
                "support": float(row['support']),
                "confidence": float(row['confidence']),
                "lift": float(row['lift'])
            })
        
        return {
            "product": product_name,
            "recommendations": recommendations_list
        }
    
    def get_recommendations(self, customer_id):
        """Get recommendations for a specific customer based on their purchase history"""
        try:
            # Get customer's purchase history
            query = """
            SELECT DISTINCT ap.product_name
            FROM amazon_orders ao
            JOIN amazon_order_items aoi ON ao.order_id = aoi.order_id
            JOIN amazon_products ap ON aoi.sku = ap.sku
            WHERE ao.ship_postal_code = %s
            AND ap.product_name IS NOT NULL
            """
            
            customer_products = self.db_manager.execute_query(query, (customer_id,))
            
            if customer_products.empty:
                return {"error": "No purchase history found for customer"}
            
            # Get recommendations based on their purchase history
            all_recommendations = []
            for _, row in customer_products.iterrows():
                product = row['product_name']
                recs = self.get_product_recommendations(product, limit=5)
                if "recommendations" in recs:
                    all_recommendations.extend(recs["recommendations"])
            
            # Remove duplicates and sort by confidence
            if all_recommendations:
                df_recs = pd.DataFrame(all_recommendations)
                df_recs = df_recs.drop_duplicates().nlargest(10, 'confidence')
                
                recommendations_list = []
                for _, row in df_recs.iterrows():
                    recommendations_list.append({
                        "antecedents": list(row['antecedents']),
                        "consequents": list(row['consequents']),
                        "support": float(row['support']),
                        "confidence": float(row['confidence']),
                        "lift": float(row['lift'])
                    })
                return {"recommendations": recommendations_list}
            else:
                return {"error": "No recommendations available"}
                
        except Exception as e:
            return {"error": f"Failed to get recommendations: {str(e)}"}
    
    def get_insights(self):
        """Get key insights from the analysis"""
        if self.rules is None:
            return {"error": "No analysis results available"}
        
        # Convert to JSON-serializable format
        strongest_associations = []
        for _, row in self.rules.nlargest(5, 'lift').iterrows():
            strongest_associations.append({
                "antecedents": list(row['antecedents']),
                "consequents": list(row['consequents']),
                "support": float(row['support']),
                "confidence": float(row['confidence']),
                "lift": float(row['lift'])
            })
        
        highest_confidence_rules = []
        for _, row in self.rules.nlargest(5, 'confidence').iterrows():
            highest_confidence_rules.append({
                "antecedents": list(row['antecedents']),
                "consequents": list(row['consequents']),
                "support": float(row['support']),
                "confidence": float(row['confidence']),
                "lift": float(row['lift'])
            })
        
        most_frequent_itemsets = []
        for _, row in self.frequent_itemsets.nlargest(5, 'support').iterrows():
            most_frequent_itemsets.append({
                "support": float(row['support']),
                "itemsets": list(row['itemsets'])
            })
        
        insights = {
            "strongest_associations": strongest_associations,
            "highest_confidence_rules": highest_confidence_rules,
            "most_frequent_itemsets": most_frequent_itemsets
        }
        
        return insights

