#!/usr/bin/env python3
"""
Demo Render Deployment Entry Point
Works without database connection
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
        
        print(f"🚀 Starting E-Commerce Market Basket Analysis DEMO")
        print(f"🌐 Host: {host}")
        print(f"📊 Port: {port}")
        print(f"📁 Working Directory: {os.getcwd()}")
        print("⚠️  Running in DEMO mode - no database required")
        print("=" * 50)
        
        # Run the demo app
        app.run(host=host, port=port, debug=False, threaded=True)
        
except Exception as e:
    print(f"❌ Error starting demo app: {e}")
    print(f"📁 Current directory: {os.getcwd()}")
    print(f"📂 Files in current directory: {os.listdir('.')}")
    if os.path.exists('app'):
        print(f"📂 Files in app directory: {os.listdir('app')}")
    sys.exit(1)
