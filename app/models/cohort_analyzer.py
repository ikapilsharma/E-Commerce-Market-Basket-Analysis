import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from database.db_manager import DatabaseManager

class CohortAnalyzer:
    def __init__(self):
        self.db_manager = DatabaseManager()
    
    def calculate_cohort_analysis(self, cohort_period='month'):
        """Calculate customer cohort analysis"""
        try:
            # Get customer order data
            query = """
            SELECT 
                ao.ship_postal_code as customer_id,
                ao.date as order_date,
                aoi.amount as order_value
            FROM amazon_orders ao
            JOIN amazon_order_items aoi ON ao.order_id = aoi.order_id
            WHERE ao.ship_postal_code IS NOT NULL
            AND ao.date >= '2022-01-01'
            ORDER BY ao.ship_postal_code, ao.date
            """
            
            df = self.db_manager.execute_query(query)
            
            if df.empty:
                return {"error": "No customer data available"}
            
            # Convert dates
            df['order_date'] = pd.to_datetime(df['order_date'])
            
            # Create cohort groups
            if cohort_period == 'month':
                df['cohort_period'] = df['order_date'].dt.to_period('M')
                df['order_period'] = df['order_date'].dt.to_period('M')
            else:  # week
                df['cohort_period'] = df['order_date'].dt.to_period('W')
                df['order_period'] = df['order_date'].dt.to_period('W')
            
            # Get first order for each customer
            df['first_order'] = df.groupby('customer_id')['order_date'].transform('min')
            if cohort_period == 'month':
                df['cohort_group'] = df['first_order'].dt.to_period('M')
            else:
                df['cohort_group'] = df['first_order'].dt.to_period('W')
            
            # Calculate cohort data
            cohort_data = df.groupby(['cohort_group', 'order_period']).agg({
                'customer_id': 'nunique',
                'order_value': 'sum'
            }).reset_index()
            
            cohort_data.columns = ['cohort_group', 'order_period', 'customer_count', 'revenue']
            
            # Create cohort table
            cohort_table = cohort_data.pivot(index='cohort_group', columns='order_period', values='customer_count')
            cohort_table = cohort_table.fillna(0)
            
            # Calculate retention rates
            cohort_sizes = cohort_table.iloc[:, 0]  # First period customer count
            retention_table = cohort_table.divide(cohort_sizes, axis=0)
            
            # Handle division by zero and infinite values
            retention_table = retention_table.replace([np.inf, -np.inf], 0)
            retention_table = retention_table.fillna(0)
            
            # Convert to JSON-serializable format
            cohort_periods = [str(period) for period in cohort_table.index]
            order_periods = [str(period) for period in cohort_table.columns]
            
            retention_data = []
            for i, cohort_period in enumerate(cohort_periods):
                row_data = {
                    "cohort_period": cohort_period,
                    "cohort_size": int(cohort_sizes.iloc[i]),
                    "retention_rates": []
                }
                
                for j, order_period in enumerate(order_periods):
                    retention_rate = float(retention_table.iloc[i, j]) if not pd.isna(retention_table.iloc[i, j]) else 0.0
                    # Ensure retention rate is valid (not infinity or NaN)
                    if retention_rate == float('inf') or retention_rate == float('-inf') or pd.isna(retention_rate):
                        retention_rate = 0.0
                    row_data["retention_rates"].append({
                        "order_period": order_period,
                        "retention_rate": round(retention_rate, 3)
                    })
                
                retention_data.append(row_data)
            
            # Calculate average retention by period
            avg_retention = []
            for j, order_period in enumerate(order_periods):
                period_retention = [row["retention_rates"][j]["retention_rate"] for row in retention_data if j < len(row["retention_rates"])]
                # Filter out invalid values
                valid_retention = [r for r in period_retention if r != float('inf') and r != float('-inf') and not pd.isna(r)]
                avg_retention.append({
                    "period": order_period,
                    "avg_retention": round(sum(valid_retention) / len(valid_retention), 3) if valid_retention else 0.0
                })
            
            return {
                "cohort_data": retention_data,
                "avg_retention": avg_retention,
                "cohort_periods": cohort_periods,
                "order_periods": order_periods,
                "total_cohorts": len(cohort_periods)
            }
            
        except Exception as e:
            return {"error": f"Cohort analysis failed: {str(e)}"}
    
    def get_cohort_insights(self):
        """Get insights from cohort analysis"""
        try:
            cohort_result = self.calculate_cohort_analysis()
            if "error" in cohort_result:
                return cohort_result
            
            insights = {
                "retention_trends": [],
                "key_metrics": {},
                "recommendations": []
            }
            
            # Calculate retention trends
            for period_data in cohort_result["avg_retention"][:6]:  # First 6 periods
                insights["retention_trends"].append({
                    "period": period_data["period"],
                    "retention_rate": period_data["avg_retention"]
                })
            
            # Key metrics
            first_period_retention = cohort_result["avg_retention"][1]["avg_retention"] if len(cohort_result["avg_retention"]) > 1 else 0
            third_period_retention = cohort_result["avg_retention"][3]["avg_retention"] if len(cohort_result["avg_retention"]) > 3 else 0
            
            insights["key_metrics"] = {
                "avg_first_period_retention": round(first_period_retention * 100, 1),
                "avg_third_period_retention": round(third_period_retention * 100, 1),
                "retention_trend": "improving" if third_period_retention > first_period_retention else "declining"
            }
            
            # Recommendations
            if first_period_retention < 0.3:
                insights["recommendations"].append("Implement onboarding improvements - low first-period retention")
            if third_period_retention < 0.2:
                insights["recommendations"].append("Focus on mid-term engagement strategies")
            
            insights["recommendations"].extend([
                "Create targeted retention campaigns for at-risk cohorts",
                "Implement loyalty programs to improve long-term retention",
                "Analyze successful cohorts to replicate strategies"
            ])
            
            return insights
            
        except Exception as e:
            return {"error": f"Failed to generate cohort insights: {str(e)}"}
