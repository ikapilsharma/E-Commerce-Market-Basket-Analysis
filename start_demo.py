#!/usr/bin/env python3
"""
Demo version for GitHub Codespaces (no database required)
"""

import os
import sys
import json

# Set environment variables
os.environ['SECRET_KEY'] = 'demo-secret-key-12345'
os.environ['FLASK_ENV'] = 'development'

def create_demo_app():
    """Create a simple demo Flask app"""
    from flask import Flask, render_template_string, jsonify
    
    app = Flask(__name__)
    
    # Demo data
    demo_data = {
        "total_revenue": 77521210,
        "total_orders": 119764,
        "total_customers": 9443,
        "avg_order_value": 647.21,
        "total_products": 10914
    }
    
    @app.route('/')
    def landing():
        return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>E-Commerce Market Basket Analysis - Demo</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
                .container { max-width: 800px; margin: 0 auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                h1 { color: #2563eb; text-align: center; }
                .stats { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 30px 0; }
                .stat-card { background: #f8fafc; padding: 20px; border-radius: 8px; text-align: center; border-left: 4px solid #2563eb; }
                .stat-number { font-size: 2em; font-weight: bold; color: #2563eb; }
                .stat-label { color: #6b7280; margin-top: 5px; }
                .features { margin: 30px 0; }
                .feature { background: #ecfdf5; padding: 15px; margin: 10px 0; border-radius: 5px; border-left: 4px solid #10b981; }
                .demo-note { background: #fef3c7; padding: 15px; border-radius: 5px; border-left: 4px solid #f59e0b; margin: 20px 0; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 E-Commerce Market Basket Analysis</h1>
                
                <div class="demo-note">
                    <strong>📊 Demo Mode:</strong> This is a simplified version running in GitHub Codespaces. 
                    The full application with database and ML models would be deployed on a cloud platform.
                </div>
                
                <div class="stats">
                    <div class="stat-card">
                        <div class="stat-number">${{ "%.1f"|format(data.total_revenue/1000000) }}M</div>
                        <div class="stat-label">Total Revenue</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{{ "{:,}".format(data.total_orders) }}</div>
                        <div class="stat-label">Total Orders</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">{{ "{:,}".format(data.total_customers) }}</div>
                        <div class="stat-label">Total Customers</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-number">${{ "%.2f"|format(data.avg_order_value) }}</div>
                        <div class="stat-label">Avg Order Value</div>
                    </div>
                </div>
                
                <div class="features">
                    <h2>🎯 Key Features</h2>
                    <div class="feature">
                        <strong>📈 Market Basket Analysis:</strong> Identifies products frequently bought together
                    </div>
                    <div class="feature">
                        <strong>👥 Customer Segmentation:</strong> Groups customers by behavior patterns
                    </div>
                    <div class="feature">
                        <strong>🔮 Sales Forecasting:</strong> Predicts future demand using ML models
                    </div>
                    <div class="feature">
                        <strong>📊 Interactive Dashboards:</strong> Real-time analytics and visualizations
                    </div>
                </div>
                
                <div class="demo-note">
                    <strong>🚀 Full Deployment:</strong> To see the complete application with all features, 
                    this would be deployed to Railway, Render, or Vercel with a PostgreSQL database.
                </div>
            </div>
        </body>
        </html>
        """, data=demo_data)
    
    @app.route('/api/stats')
    def api_stats():
        return jsonify(demo_data)
    
    @app.route('/dashboard')
    def dashboard():
        return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Analytics Dashboard - Demo</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
                .container { max-width: 1000px; margin: 0 auto; background: white; padding: 40px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                h1 { color: #2563eb; text-align: center; }
                .chart-placeholder { background: #f8fafc; border: 2px dashed #cbd5e1; padding: 60px; text-align: center; border-radius: 8px; margin: 20px 0; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>📊 Analytics Dashboard</h1>
                <div class="chart-placeholder">
                    <h3>📈 Sales Trends Chart</h3>
                    <p>In the full version, this would show interactive charts with real data</p>
                </div>
                <div class="chart-placeholder">
                    <h3>🛒 Market Basket Analysis</h3>
                    <p>Product associations and cross-selling opportunities</p>
                </div>
                <div class="chart-placeholder">
                    <h3>👥 Customer Segments</h3>
                    <p>Customer behavior analysis and targeting</p>
                </div>
            </div>
        </body>
        </html>
        """)
    
    return app

def main():
    print("🚀 Starting E-Commerce Market Basket Analysis Demo")
    print("=" * 60)
    print("📊 Demo Features:")
    print("   • Landing page with key metrics")
    print("   • Analytics dashboard")
    print("   • API endpoints")
    print("=" * 60)
    print("🌐 Your demo will be available at:")
    print("   https://your-codespace-5003.preview.app.github.dev")
    print("=" * 60)
    
    app = create_demo_app()
    port = 5003
    print(f"🚀 Starting demo server on port {port}")
    
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    main()
