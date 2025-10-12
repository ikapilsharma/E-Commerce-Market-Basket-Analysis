#!/usr/bin/env python3
"""
Render Deployment Entry Point
Simple, bulletproof entry point for Render
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
        print(f"🐍 Python Path: {sys.path[:3]}")
        print("=" * 50)
        
        # Run the app
        app.run(host=host, port=port, debug=False, threaded=True)
        
except Exception as e:
    print(f"❌ Error starting app: {e}")
    print(f"📁 Current directory: {os.getcwd()}")
    print(f"📂 Files in current directory: {os.listdir('.')}")
    print(f"📂 Files in app directory: {os.listdir('app') if os.path.exists('app') else 'app directory not found'}")
    sys.exit(1)
