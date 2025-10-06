#!/usr/bin/env python3
"""
E-Commerce Market Basket Analysis Application
Production-ready Flask application with ML models and interactive dashboard
"""

import os
import sys
from app import app

if __name__ == '__main__':
    # Check if database connection is available
    try:
        from database.db_manager import DatabaseManager
        db_manager = DatabaseManager()
        connection_test = db_manager.test_connection()
        print(f"Database Status: {connection_test['status']}")
        if connection_test['status'] != 'Connected':
            print(f"Database Error: {connection_test['message']}")
            print("Please ensure PostgreSQL is running and database is accessible")
    except Exception as e:
        print(f"Database connection failed: {e}")
        print("Please check your database configuration")
    
    # Run the application
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    
    print(f"\n🚀 Starting E-Commerce Market Basket Analysis Application")
    print(f"📊 Dashboard: http://localhost:{port}")
    print(f"🏠 Landing Page: http://localhost:{port}/")
    print(f"🔧 Debug Mode: {debug}")
    print(f"📈 API Endpoints:")
    print(f"   - /api/stats - Overall statistics")
    print(f"   - /api/market-basket - Market basket analysis")
    print(f"   - /api/customer-segments - Customer segmentation")
    print(f"   - /api/sales-forecast - Sales predictions")
    print(f"   - /api/top-products - Top performing products")
    print(f"   - /api/sales-trends - Sales trends over time")
    print(f"\nPress Ctrl+C to stop the server\n")
    
    app.run(host='0.0.0.0', port=port, debug=debug)

