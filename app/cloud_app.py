#!/usr/bin/env python3
"""
Cloud-ready App Runner for E-Commerce Analytics Platform
Optimized for Railway, Render, Heroku, and other cloud platforms
"""

import os
import sys
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the app directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the main app
from app import app

def setup_cloud_logging(app):
    """Setup cloud-optimized logging"""
    # Cloud platforms handle logging differently
    if not app.debug:
        app.logger.setLevel(logging.INFO)
        app.logger.info('E-Commerce Analytics Platform starting in cloud mode')

def create_cloud_app():
    """Create and configure the Flask app for cloud deployment"""
    
    # Get port from environment (required for cloud platforms)
    port = int(os.getenv('PORT', 5003))
    
    # Configure for cloud deployment
    app.config.update(
        SECRET_KEY=os.getenv('SECRET_KEY', 'cloud-secret-key-change-in-production'),
        DEBUG=False,
        TESTING=False,
        HOST='0.0.0.0',  # Required for cloud platforms
        PORT=port
    )
    
    # Setup logging
    setup_cloud_logging(app)
    
    return app

if __name__ == '__main__':
    app_instance = create_cloud_app()
    
    # Get configuration from environment
    host = '0.0.0.0'  # Cloud platforms require 0.0.0.0
    port = int(os.getenv('PORT', 5003))
    
    print("🚀 Starting E-Commerce Analytics Platform (Cloud Mode)")
    print("=" * 60)
    print(f"🌐 Server: http://0.0.0.0:{port}")
    print(f"📊 Executive Dashboard: http://0.0.0.0:{port}/advanced-dashboard")
    print(f"📈 Analytics Dashboard: http://0.0.0.0:{port}/dashboard")
    print(f"🏠 Landing Page: http://0.0.0.0:{port}/")
    print("=" * 60)
    print("☁️ Cloud deployment features:")
    print("   • Auto-scaling enabled")
    print("   • Cloud logging")
    print("   • Environment-based config")
    print("   • Production security")
    print("=" * 60)
    
    try:
        app_instance.run(
            host=host,
            port=port,
            debug=False,  # Always False in cloud
            threaded=True
        )
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)
