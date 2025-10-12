#!/usr/bin/env python3
"""
Standalone Demo App - No Database Required
Complete E-Commerce Market Basket Analysis Demo
"""

import os
import sys
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import json
from datetime import datetime, timedelta
import numpy as np

# Create Flask app with correct template folder
app = Flask(__name__, template_folder='app/templates')
CORS(app)

# Demo data
DEMO_STATS = {
    'total_revenue': 77521210.0,
    'total_orders': 119764,
    'total_products': 10914,
    'avg_order_value': 647.21,
    'total_customers': 9443,
    'date_range': {
        'start_date': '2022-03-31',
        'end_date': '2022-06-29'
    }
}

@app.route('/')
def landing_page():
    """Landing page"""
    return render_template('landing.html')

@app.route('/dashboard')
def dashboard():
    """Main dashboard"""
    return render_template('dashboard_fixed.html')

@app.route('/advanced-dashboard')
def advanced_dashboard():
    """Advanced dashboard"""
    return render_template('advanced_dashboard.html')

@app.route('/api/stats')
def get_stats():
    """Get overall statistics"""
    return jsonify(DEMO_STATS)

@app.route('/api/market-basket')
def get_market_basket_analysis():
    """Market basket analysis with demo data"""
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
            "total_transactions": DEMO_STATS['total_orders'],
            "frequent_itemsets_count": 15,
            "association_rules_count": len(demo_rules)
        }
    }
    
    return jsonify(results)

@app.route('/api/customer-segments')
def get_customer_segments():
    """Customer segmentation with demo data"""
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

@app.route('/api/sales-forecast')
def get_sales_forecast():
    """Sales forecast with demo data"""
    months_ahead = request.args.get('months', 3, type=int)
    
    base_date = datetime.now()
    predictions = []
    base_revenue = 2500000
    
    for i in range(1, months_ahead + 1):
        future_date = base_date + timedelta(days=30 * i)
        variation = 1.0 + (i * 0.05)  # 5% growth trend
        predicted_revenue = base_revenue * variation
        predicted_orders = int(predicted_revenue / 730)
        
        predictions.append({
            "date": future_date.strftime('%Y-%m-%d'),
            "predicted_revenue": round(predicted_revenue, 2),
            "predicted_orders": predicted_orders,
            "predicted_avg_order_value": round(predicted_revenue / predicted_orders, 2)
        })
    
    total_predicted_revenue = sum(p['predicted_revenue'] for p in predictions)
    
    forecast = {
        "predictions": predictions,
        "summary": {
            "total_predicted_revenue": round(total_predicted_revenue, 2),
            "total_predicted_orders": sum(p['predicted_orders'] for p in predictions),
            "avg_daily_revenue": round(total_predicted_revenue / len(predictions), 2),
            "forecast_period_days": months_ahead * 30
        }
    }
    
    return jsonify(forecast)

@app.route('/api/top-products')
def get_top_products():
    """Top products with demo data"""
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

@app.route('/api/sales-trends')
def get_sales_trends():
    """Sales trends with demo data"""
    trends = [
        {"month": "2022-01", "orders": 28500, "revenue": 20850000, "avg_order_value": 731.58},
        {"month": "2022-02", "orders": 31200, "revenue": 22800000, "avg_order_value": 730.77},
        {"month": "2022-03", "orders": 29800, "revenue": 21770000, "avg_order_value": 730.54},
        {"month": "2022-04", "orders": 30200, "revenue": 22080000, "avg_order_value": 731.13},
        {"month": "2022-05", "orders": 31800, "revenue": 23240000, "avg_order_value": 730.82},
        {"month": "2022-06", "orders": 29500, "revenue": 21560000, "avg_order_value": 730.85}
    ]
    
    return jsonify(trends)

@app.route('/api/rfm-analysis')
def api_rfm_analysis():
    """RFM Analysis with demo data"""
    rfm_data = {
        "rfm_data": [
            {"segment": "Champions", "count": 1500, "percentage": 12.5, "monetary": 8500},
            {"segment": "Loyal Customers", "count": 2800, "percentage": 23.3, "monetary": 4200},
            {"segment": "Potential Loyalists", "count": 3200, "percentage": 26.7, "monetary": 1800},
            {"segment": "New Customers", "count": 1800, "percentage": 15.0, "monetary": 450},
            {"segment": "Promising", "count": 1200, "percentage": 10.0, "monetary": 650},
            {"segment": "Need Attention", "count": 800, "percentage": 6.7, "monetary": 320},
            {"segment": "About to Sleep", "count": 400, "percentage": 3.3, "monetary": 280},
            {"segment": "At Risk", "count": 300, "percentage": 2.5, "monetary": 150}
        ],
        "summary": {
            "total_customers": 12000,
            "high_value_customers": 4300,
            "retention_rate": 73.5
        }
    }
    return jsonify(rfm_data)

@app.route('/api/cohort-analysis')
def api_cohort_analysis():
    """Cohort Analysis with demo data"""
    cohort_data = {
        "cohort_data": [
            {"cohort": "2022-01", "size": 2500, "retention_rates": [100, 82, 70, 66, 63, 60, 58, 56, 54, 52, 50, 48]},
            {"cohort": "2022-02", "size": 2800, "retention_rates": [100, 85, 73, 69, 66, 63, 61, 59, 57, 55, 53, 51]},
            {"cohort": "2022-03", "size": 2600, "retention_rates": [100, 87, 74, 70, 67, 64, 62, 60, 58, 56, 54, 52]},
            {"cohort": "2022-04", "size": 2900, "retention_rates": [100, 84, 71, 67, 64, 61, 59, 57, 55, 53, 51, 49]},
            {"cohort": "2022-05", "size": 3000, "retention_rates": [100, 86, 73, 69, 66, 63, 61, 59, 57, 55, 53, 51]},
            {"cohort": "2022-06", "size": 2700, "retention_rates": [100, 83, 70, 66, 63, 60, 58, 56, 54, 52, 50, 48]}
        ],
        "avg_retention": [
            {"period": 0, "avg_retention": 1.00},
            {"period": 1, "avg_retention": 0.85},
            {"period": 2, "avg_retention": 0.72},
            {"period": 3, "avg_retention": 0.68},
            {"period": 4, "avg_retention": 0.65},
            {"period": 5, "avg_retention": 0.62},
            {"period": 6, "avg_retention": 0.60},
            {"period": 7, "avg_retention": 0.58},
            {"period": 8, "avg_retention": 0.56},
            {"period": 9, "avg_retention": 0.54},
            {"period": 10, "avg_retention": 0.52},
            {"period": 11, "avg_retention": 0.50}
        ],
        "summary": {
            "avg_retention_rate": 73.5,
            "best_performing_cohort": "2022-03",
            "total_cohorts": 6
        }
    }
    return jsonify(cohort_data)

@app.route('/api/executive-summary')
def api_executive_summary():
    """Executive summary with demo data"""
    summary = {
        "total_revenue": 77521210.0,
        "total_orders": 119764,
        "total_customers": 9443,
        "avg_order_value": 647.21,
        "growth_rate": 15.2,
        "top_category": "Kurta",
        "customer_retention": 73.5,
        "recommendations": [
            "Focus on Cotton Kurta and Designer Kurta bundle promotions",
            "Implement loyalty program for high-value customers",
            "Expand product line in the Set category",
            "Improve customer retention through targeted campaigns"
        ]
    }
    return jsonify(summary)

@app.route('/api/recommendations/<customer_id>')
def get_recommendations(customer_id):
    """Product recommendations with demo data"""
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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5003))
    host = '0.0.0.0'
    
    print(f"🚀 Starting E-Commerce Market Basket Analysis - Standalone Demo")
    print(f"🌐 Host: {host}")
    print(f"📊 Port: {port}")
    print(f"📁 Working Directory: {os.getcwd()}")
    print("📊 Using standalone demo data - no database required")
    print("🎯 All features working: Dashboard, Analytics, RFM, Cohort Analysis")
    print("=" * 70)
    
    app.run(host=host, port=port, debug=False, threaded=True)
