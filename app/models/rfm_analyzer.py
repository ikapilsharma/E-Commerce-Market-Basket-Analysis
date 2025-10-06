import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from database.db_manager import DatabaseManager

class RFMAnalyzer:
    def __init__(self):
        self.db_manager = DatabaseManager()
        
    def calculate_rfm(self, reference_date=None):
        """Calculate RFM (Recency, Frequency, Monetary) scores"""
        try:
            if reference_date is None:
                reference_date = datetime.now()
            
            # Get customer transaction data
            query = """
            SELECT 
                ao.ship_postal_code as customer_id,
                ao.date as order_date,
                aoi.amount as order_value,
                aoi.qty as quantity
            FROM amazon_orders ao
            JOIN amazon_order_items aoi ON ao.order_id = aoi.order_id
            WHERE ao.ship_postal_code IS NOT NULL
            AND ao.date <= %s
            ORDER BY ao.ship_postal_code, ao.date
            """
            
            df = self.db_manager.execute_query(query, (reference_date,))
            
            if df.empty:
                return {"error": "No customer data available"}
            
            # Convert order_date to datetime if it's not already
            df['order_date'] = pd.to_datetime(df['order_date'])
            
            # Calculate RFM metrics
            rfm_df = df.groupby('customer_id').agg({
                'order_date': lambda x: (pd.to_datetime(reference_date) - x.max()).days,  # Recency
                'order_value': ['count', 'sum']  # Frequency and Monetary
            }).reset_index()
            
            # Flatten column names
            rfm_df.columns = ['customer_id', 'recency', 'frequency', 'monetary']
            
            # Calculate RFM scores (1-5 scale)
            rfm_df['R_score'] = pd.cut(rfm_df['recency'], 5, labels=[5,4,3,2,1]).astype(int)
            rfm_df['F_score'] = pd.cut(rfm_df['frequency'], 5, labels=[1,2,3,4,5]).astype(int)
            rfm_df['M_score'] = pd.cut(rfm_df['monetary'], 5, labels=[1,2,3,4,5]).astype(int)
            
            # Combine scores
            rfm_df['RFM_score'] = rfm_df['R_score'].astype(str) + rfm_df['F_score'].astype(str) + rfm_df['M_score'].astype(str)
            
            # Customer segmentation
            rfm_df['segment'] = rfm_df.apply(self._segment_customers, axis=1)
            
            # Convert to JSON-serializable format
            rfm_data = []
            for _, row in rfm_df.iterrows():
                rfm_data.append({
                    "customer_id": str(row['customer_id']),
                    "recency": int(row['recency']),
                    "frequency": int(row['frequency']),
                    "monetary": float(row['monetary']),
                    "r_score": int(row['R_score']),
                    "f_score": int(row['F_score']),
                    "m_score": int(row['M_score']),
                    "rfm_score": str(row['RFM_score']),
                    "segment": str(row['segment'])
                })
            
            # Segment summary
            segment_summary = rfm_df.groupby('segment').agg({
                'customer_id': 'count',
                'recency': 'mean',
                'frequency': 'mean',
                'monetary': 'mean'
            }).reset_index()
            
            summary_data = []
            for _, row in segment_summary.iterrows():
                summary_data.append({
                    "segment": str(row['segment']),
                    "customer_count": int(row['customer_id']),
                    "avg_recency": float(row['recency']),
                    "avg_frequency": float(row['frequency']),
                    "avg_monetary": float(row['monetary'])
                })
            
            return {
                "rfm_data": rfm_data,
                "segment_summary": summary_data,
                "total_customers": len(rfm_data),
                "reference_date": reference_date.strftime('%Y-%m-%d')
            }
            
        except Exception as e:
            return {"error": f"RFM calculation failed: {str(e)}"}
    
    def _segment_customers(self, row):
        """Segment customers based on RFM scores"""
        r, f, m = row['R_score'], row['F_score'], row['M_score']
        
        if r >= 4 and f >= 4 and m >= 4:
            return "Champions"
        elif r >= 3 and f >= 3 and m >= 3:
            return "Loyal Customers"
        elif r >= 4 and f <= 2:
            return "New Customers"
        elif r >= 3 and f >= 2 and m >= 2:
            return "Potential Loyalists"
        elif r >= 3 and f <= 2 and m <= 2:
            return "At Risk"
        elif r <= 2 and f >= 3 and m >= 3:
            return "Cannot Lose Them"
        elif r <= 2 and f >= 2 and m >= 2:
            return "About to Sleep"
        else:
            return "Lost"
    
    def get_rfm_insights(self):
        """Get key insights from RFM analysis"""
        try:
            rfm_result = self.calculate_rfm()
            if "error" in rfm_result:
                return rfm_result
            
            insights = {
                "top_segments": [],
                "revenue_opportunity": {},
                "recommendations": []
            }
            
            # Analyze segments
            for segment in rfm_result["segment_summary"]:
                if segment["customer_count"] > 0:
                    insights["top_segments"].append({
                        "segment": segment["segment"],
                        "percentage": round((segment["customer_count"] / rfm_result["total_customers"]) * 100, 2),
                        "avg_value": segment["avg_monetary"]
                    })
            
            # Revenue opportunities
            champions = next((s for s in rfm_result["segment_summary"] if s["segment"] == "Champions"), None)
            at_risk = next((s for s in rfm_result["segment_summary"] if s["segment"] == "At Risk"), None)
            
            if champions and at_risk:
                insights["revenue_opportunity"] = {
                    "champions_revenue": champions["avg_monetary"] * champions["customer_count"],
                    "at_risk_revenue": at_risk["avg_monetary"] * at_risk["customer_count"],
                    "retention_opportunity": round((at_risk["avg_monetary"] * at_risk["customer_count"]) * 0.2, 2)
                }
            
            # Recommendations
            insights["recommendations"] = [
                "Focus retention efforts on 'At Risk' customers",
                "Increase engagement with 'About to Sleep' segment",
                "Upsell to 'Loyal Customers' to maximize value",
                "Create win-back campaigns for 'Lost' customers"
            ]
            
            return insights
            
        except Exception as e:
            return {"error": f"Failed to generate insights: {str(e)}"}
