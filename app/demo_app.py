#!/usr/bin/env python3
"""
E-Commerce Market Basket Analysis Application - Demo Version
This version works without database connection for demonstration purposes
"""

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta
import os

app = Flask(__name__)
CORS(app)

# Demo data for demonstration
DEMO_DATA = {
    'total_orders': 119764,
    'total_revenue': 87500000,
    'total_products': 9000,
    'avg_order_value': 730.45
}

@app.route('/')
def landing_page():
    """Landing page with project overview and demo"""
    return render_template('landing.html')

@app.route('/dashboard')
def dashboard():
    """Main dashboard with interactive visualizations"""
    return render_template('dashboard_fixed.html')

@app.route('/api/stats')
def get_stats():
    """Get overall statistics"""
    return jsonify(DEMO_DATA)

@app.route('/api/market-basket')
def get_market_basket_analysis():
    """Get market basket analysis results using Apriori algorithm"""
    try:
        min_support = request.args.get('min_support', 0.01, type=float)
        min_confidence = request.args.get('min_confidence', 0.3, type=float)
        
        # Demo association rules data
        demo_rules = [
            {
                'antecedents': 'Cotton Kurta',
                'consequents': 'Designer Kurta',
                'support': 0.025,
                'confidence': 0.78,
                'lift': 3.2
            },
            {
                'antecedents': 'Casual Kurta',
                'consequents': 'Cotton Kurta',
                'support': 0.022,
                'confidence': 0.72,
                'lift': 2.9
            },
            {
                'antecedents': 'Cotton Kurta',
                'consequents': 'Stylish Kurta',
                'support': 0.018,
                'confidence': 0.68,
                'lift': 2.7
            },
            {
                'antecedents': 'Casual Kurta',
                'consequents': 'Designer Kurta',
                'support': 0.016,
                'confidence': 0.65,
                'lift': 2.5
            }
        ]
        
        results = {
            "frequent_itemsets": [
                {'items': ['Cotton Kurta', 'Designer Kurta'], 'support': 0.025},
                {'items': ['Casual Kurta', 'Cotton Kurta'], 'support': 0.022},
                {'items': ['Cotton Kurta', 'Stylish Kurta'], 'support': 0.018}
            ],
            "association_rules": demo_rules,
            "summary": {
                "total_transactions": DEMO_DATA['total_orders'],
                "frequent_itemsets_count": 15,
                "association_rules_count": len(demo_rules)
            }
        }
        
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/customer-segments')
def get_customer_segments():
    """Get customer segmentation results"""
    try:
        segments = {
            "customers": [
                {"customer_id": "1001", "cluster": 0, "total_orders": 12, "total_spent": 8500, "segment": "High-Value Loyal"},
                {"customer_id": "1002", "cluster": 1, "total_orders": 8, "total_spent": 4200, "segment": "Regular High AOV"},
                {"customer_id": "1003", "cluster": 2, "total_orders": 4, "total_spent": 1800, "segment": "Growing"},
                {"customer_id": "1004", "cluster": 3, "total_orders": 1, "total_spent": 450, "segment": "New/Infrequent"}
            ],
            "cluster_profiles": {
                "Cluster_0": {
                    "size": 1500,
                    "avg_total_orders": 12.5,
                    "avg_total_spent": 8500,
                    "characteristics": "High-Value Loyal Customers"
                },
                "Cluster_1": {
                    "size": 2800,
                    "avg_total_orders": 8.2,
                    "avg_total_spent": 4200,
                    "characteristics": "Regular Customers with High AOV"
                },
                "Cluster_2": {
                    "size": 3200,
                    "avg_total_orders": 4.1,
                    "avg_total_spent": 1800,
                    "characteristics": "Growing Customers"
                },
                "Cluster_3": {
                    "size": 4500,
                    "avg_total_orders": 1.2,
                    "avg_total_spent": 450,
                    "characteristics": "New/Infrequent Customers"
                }
            },
            "summary": {
                "total_customers": 12000,
                "clusters": 4
            }
        }
        return jsonify(segments)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/sales-forecast')
def get_sales_forecast():
    """Get sales forecast predictions"""
    try:
        months_ahead = request.args.get('months', 3, type=int)
        
        # Generate demo forecast data
        base_date = datetime.now()
        predictions = []
        base_revenue = 2500000
        
        for i in range(1, months_ahead + 1):
            future_date = base_date + timedelta(days=30 * i)
            # Add some realistic variation
            variation = np.random.normal(1.0, 0.1)
            predicted_revenue = base_revenue * variation * (1 + i * 0.05)  # 5% growth trend
            predicted_orders = int(predicted_revenue / 730)  # Based on avg order value
            
            predictions.append({
                "date": future_date.strftime('%Y-%m-%d'),
                "predicted_revenue": round(predicted_revenue, 2),
                "predicted_orders": predicted_orders,
                "predicted_avg_order_value": round(predicted_revenue / predicted_orders, 2)
            })
        
        total_predicted_revenue = sum(p['predicted_revenue'] for p in predictions)
        avg_daily_revenue = total_predicted_revenue / len(predictions)
        
        forecast = {
            "predictions": predictions,
            "summary": {
                "total_predicted_revenue": round(total_predicted_revenue, 2),
                "total_predicted_orders": sum(p['predicted_orders'] for p in predictions),
                "avg_daily_revenue": round(avg_daily_revenue, 2),
                "forecast_period_days": months_ahead * 30
            }
        }
        
        return jsonify(forecast)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/top-products')
def get_top_products():
    """Get top performing products"""
    try:
        limit = request.args.get('limit', 20, type=int)
        
        products = [
            {"product_name": "Cotton Kurta", "category": "Kurta", "total_revenue": 2500000, "order_count": 3420},
            {"product_name": "Designer Kurta", "category": "Kurta", "total_revenue": 2200000, "order_count": 2890},
            {"product_name": "Casual Kurta", "category": "Kurta", "total_revenue": 1800000, "order_count": 2560},
            {"product_name": "Stylish Kurta", "category": "Kurta", "total_revenue": 1500000, "order_count": 2100},
            {"product_name": "Elegant Set", "category": "Set", "total_revenue": 1200000, "order_count": 1800},
            {"product_name": "Designer Set", "category": "Set", "total_revenue": 1100000, "order_count": 1650},
            {"product_name": "Formal Set", "category": "Set", "total_revenue": 950000, "order_count": 1420},
            {"product_name": "Casual Set", "category": "Set", "total_revenue": 850000, "order_count": 1280},
            {"product_name": "Evening Dress", "category": "Western Dress", "total_revenue": 750000, "order_count": 1150},
            {"product_name": "Summer Dress", "category": "Western Dress", "total_revenue": 680000, "order_count": 980}
        ]
        
        return jsonify(products[:limit])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/sales-trends')
def get_sales_trends():
    """Get sales trends over time"""
    try:
        trends = [
            {"month": "2022-01", "orders": 28500, "revenue": 20850000, "avg_order_value": 731.58},
            {"month": "2022-02", "orders": 31200, "revenue": 22800000, "avg_order_value": 730.77},
            {"month": "2022-03", "orders": 29800, "revenue": 21770000, "avg_order_value": 730.54},
            {"month": "2022-04", "orders": 30200, "revenue": 22080000, "avg_order_value": 731.13}
        ]
        
        return jsonify(trends)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/recommendations/<customer_id>')
def get_recommendations(customer_id):
    """Get product recommendations for a specific customer"""
    try:
        recommendations = [
            {
                "product": "Designer Kurta",
                "confidence": 0.78,
                "reason": "Customers who bought Cotton Kurta also bought Designer Kurta"
            },
            {
                "product": "Stylish Kurta", 
                "confidence": 0.68,
                "reason": "Frequently bought together with Cotton Kurta"
            },
            {
                "product": "Elegant Set",
                "confidence": 0.55,
                "reason": "Popular among similar customers"
            }
        ]
        
        return jsonify({"recommendations": recommendations})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"\n🚀 Starting E-Commerce Market Basket Analysis Application (Demo Mode)")
    print(f"📊 Dashboard: http://localhost:{port}/dashboard")
    print(f"🏠 Landing Page: http://localhost:{port}/")
    print(f"🔧 Debug Mode: {debug}")
    print(f"📈 API Endpoints:")
    print(f"   - /api/stats - Overall statistics")
    print(f"   - /api/market-basket - Market basket analysis")
    print(f"   - /api/customer-segments - Customer segmentation")
    print(f"   - /api/sales-forecast - Sales predictions")
    print(f"   - /api/top-products - Top performing products")
    print(f"   - /api/sales-trends - Sales trends over time")
    print(f"\n🎯 This is a DEMO version with sample data")
    print(f"💡 To connect to your actual database, use the full app.py version")
    print(f"\n✨ NEW: Improved organized dashboard with proper alignment!")
    print(f"\nPress Ctrl+C to stop the server\n")
    
    app.run(host='0.0.0.0', port=port, debug=debug)
