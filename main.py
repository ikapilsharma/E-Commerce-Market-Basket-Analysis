#!/usr/bin/env python3
"""
Railway Deployment Entry Point
Simple entry point for Railway deployment
"""

import os
import sys

# Add the app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

# Import and run the Flask app
from app import app

if __name__ == '__main__':
    # Get port from environment (Railway sets this)
    port = int(os.environ.get('PORT', 5003))
    host = os.environ.get('HOST', '0.0.0.0')
    
    print(f"🚀 Starting E-Commerce Market Basket Analysis on {host}:{port}")
    
    # Run the application
    app.run(host=host, port=port, debug=False)
