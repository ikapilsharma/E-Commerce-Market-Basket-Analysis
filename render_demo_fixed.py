#!/usr/bin/env python3
"""
Fixed Demo Render Deployment Entry Point
Works with sample data instead of requiring database setup
"""

import os
import sys

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

try:
    # Import the demo app directly
    import demo_app
    
    if __name__ == '__main__':
        # Get port from environment
        port = int(os.environ.get('PORT', 5003))
        host = '0.0.0.0'
        
        print(f"🚀 Starting E-Commerce Market Basket Analysis with Demo Data")
        print(f"🌐 Host: {host}")
        print(f"📊 Port: {port}")
        print(f"📁 Working Directory: {os.getcwd()}")
        print("📊 Using demo data - no database required")
        print("🎯 Features: Landing page, Dashboard, Advanced Analytics")
        print("=" * 60)
        
        # Run the demo app
        demo_app.app.run(host=host, port=port, debug=False, threaded=True)
        
except Exception as e:
    print(f"❌ Error starting demo app: {e}")
    print(f"📁 Current directory: {os.getcwd()}")
    print(f"📂 Files in current directory: {os.listdir('.')}")
    if os.path.exists('app'):
        print(f"📂 Files in app directory: {os.listdir('app')}")
    
    # Fallback: create a simple working demo
    print("🔄 Creating fallback demo app...")
    
    from flask import Flask, render_template, jsonify
    from flask_cors import CORS
    
    fallback_app = Flask(__name__)
    CORS(fallback_app)
    
    @fallback_app.route('/')
    def landing():
        return render_template('landing.html')
    
    @fallback_app.route('/dashboard')
    def dashboard():
        return render_template('dashboard_fixed.html')
    
    @fallback_app.route('/advanced-dashboard')
    def advanced_dashboard():
        return render_template('advanced_dashboard.html')
    
    @fallback_app.route('/api/stats')
    def get_stats():
        return jsonify({
            'total_revenue': 77521210.0,
            'total_orders': 119764,
            'total_products': 10914,
            'avg_order_value': 647.21,
            'total_customers': 9443
        })
    
    @fallback_app.route('/api/market-basket')
    def get_market_basket():
        return jsonify({
            'association_rules': [
                {
                    'antecedents': 'Cotton Kurta',
                    'consequents': 'Designer Kurta',
                    'support': 0.025,
                    'confidence': 0.78,
                    'lift': 3.2
                }
            ],
            'frequent_itemsets': [
                {'items': ['Cotton Kurta', 'Designer Kurta'], 'support': 0.025}
            ]
        })
    
    @fallback_app.route('/api/customer-segments')
    def get_customer_segments():
        return jsonify({
            'customers': [
                {'customer_id': '1001', 'segment': 'High-Value', 'total_orders': 12, 'total_spent': 8500}
            ],
            'cluster_profiles': {
                'Cluster_0': {'size': 1500, 'characteristics': 'High-Value Loyal Customers'}
            }
        })
    
    @fallback_app.route('/api/sales-forecast')
    def get_sales_forecast():
        return jsonify({
            'predictions': [
                {'date': '2024-01-01', 'predicted_revenue': 2500000, 'predicted_orders': 3420}
            ]
        })
    
    @fallback_app.route('/api/top-products')
    def get_top_products():
        return jsonify([
            {'product_name': 'Cotton Kurta', 'total_revenue': 2500000, 'order_count': 3420}
        ])
    
    @fallback_app.route('/api/sales-trends')
    def get_sales_trends():
        return jsonify([
            {'month': '2022-01', 'orders': 28500, 'revenue': 20850000}
        ])
    
    @fallback_app.route('/api/rfm-analysis')
    def api_rfm_analysis():
        return jsonify({
            'rfm_data': {
                'champions': 1500,
                'loyal_customers': 2800,
                'potential_loyalists': 3200
            }
        })
    
    @fallback_app.route('/api/cohort-analysis')
    def api_cohort_analysis():
        return jsonify({
            'cohort_data': {
                'retention_rates': [100, 85, 72, 68]
            }
        })
    
    @fallback_app.route('/api/executive-summary')
    def api_executive_summary():
        return jsonify({
            'total_revenue': 77521210.0,
            'total_orders': 119764,
            'total_customers': 9443
        })
    
    print("✅ Fallback demo app created successfully!")
    port = int(os.environ.get('PORT', 5003))
    fallback_app.run(host='0.0.0.0', port=port, debug=False, threaded=True)
