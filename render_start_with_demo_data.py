#!/usr/bin/env python3
"""
Render Deployment with Demo Data
Works with sample data instead of requiring database setup
"""

import os
import sys

# Add app directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

try:
    # Import the demo app that works without database
    from app.demo_app import app
    
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
        app.run(host=host, port=port, debug=False, threaded=True)
        
except Exception as e:
    print(f"❌ Error starting demo app: {e}")
    print(f"📁 Current directory: {os.getcwd()}")
    if os.path.exists('app'):
        print(f"📂 Files in app directory: {os.listdir('app')}")
    sys.exit(1)
