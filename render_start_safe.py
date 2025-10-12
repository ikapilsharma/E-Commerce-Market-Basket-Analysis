#!/usr/bin/env python3
"""
Safe Render Deployment Entry Point
Handles database connection failures gracefully
"""

import os
import sys

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

try:
    # Import Flask app
    from app import app
    
    if __name__ == '__main__':
        # Get port from environment
        port = int(os.environ.get('PORT', 5003))
        host = '0.0.0.0'
        
        print(f"🚀 Starting E-Commerce Market Basket Analysis")
        print(f"🌐 Host: {host}")
        print(f"📊 Port: {port}")
        print(f"📁 Working Directory: {os.getcwd()}")
        
        # Test database connection
        try:
            from app.database.db_manager import DatabaseManager
            db = DatabaseManager()
            conn = db.get_connection()
            if conn:
                print("✅ Database connection successful")
                conn.close()
            else:
                print("⚠️  Database connection failed - app will run with limited functionality")
        except Exception as e:
            print(f"⚠️  Database test failed: {e} - app will run with limited functionality")
        
        print("=" * 50)
        
        # Run the app
        app.run(host=host, port=port, debug=False, threaded=True)
        
except Exception as e:
    print(f"❌ Error starting app: {e}")
    print(f"📁 Current directory: {os.getcwd()}")
    print(f"📂 Files in current directory: {os.listdir('.')}")
    if os.path.exists('app'):
        print(f"📂 Files in app directory: {os.listdir('app')}")
    sys.exit(1)
