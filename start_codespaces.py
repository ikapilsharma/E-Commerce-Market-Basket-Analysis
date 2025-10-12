#!/usr/bin/env python3
"""
Start script for GitHub Codespaces
"""

import os
import sys
import subprocess

# Set environment variables for Codespaces
os.environ['DB_HOST'] = 'localhost'
os.environ['DB_NAME'] = 'mba_db'
os.environ['DB_USER'] = 'postgres'
os.environ['DB_PASSWORD'] = 'postgres'
os.environ['DB_PORT'] = '5432'
os.environ['SECRET_KEY'] = 'codespaces-secret-key-12345'
os.environ['FLASK_ENV'] = 'development'

def start_app():
    """Start the Flask application"""
    print("🚀 Starting E-Commerce Market Basket Analysis in GitHub Codespaces")
    print("=" * 60)
    print("📊 Features:")
    print("   • Market Basket Analysis")
    print("   • Customer Segmentation")
    print("   • Sales Forecasting")
    print("   • Interactive Dashboards")
    print("=" * 60)
    print("🌐 Your app will be available at:")
    print("   https://your-codespace-5003.preview.app.github.dev")
    print("=" * 60)
    
    # Add app directory to path
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))
    
    # Import and run the app
    from app import app
    
    port = 5003
    print(f"🚀 Starting server on port {port}")
    
    app.run(host='0.0.0.0', port=port, debug=True)

if __name__ == '__main__':
    start_app()
