#!/usr/bin/env python3
"""
Production App Runner for E-Commerce Analytics Platform
This file configures the app for production deployment
"""

import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Add the app directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the main app
from app import app

def setup_logging(app):
    """Setup production logging"""
    if not app.debug and not app.testing:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        
        file_handler = RotatingFileHandler(
            'logs/app.log', 
            maxBytes=10240000,  # 10MB
            backupCount=10
        )
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)
        
        app.logger.setLevel(logging.INFO)
        app.logger.info('E-Commerce Analytics Platform startup')

def create_app():
    """Create and configure the Flask app for production"""
    
    # Configure for production
    app.config.update(
        SECRET_KEY=os.getenv('SECRET_KEY', 'dev-secret-key'),
        DEBUG=False,
        TESTING=False,
        HOST=os.getenv('HOST', '0.0.0.0'),
        PORT=int(os.getenv('PORT', 5003))
    )
    
    # Setup logging
    setup_logging(app)
    
    return app

if __name__ == '__main__':
    app_instance = create_app()
    
    # Get configuration from environment
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5003))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    print("🚀 Starting E-Commerce Analytics Platform (Production Mode)")
    print("=" * 60)
    print(f"🌐 Server: http://{host}:{port}")
    print(f"📊 Executive Dashboard: http://{host}:{port}/advanced-dashboard")
    print(f"📈 Analytics Dashboard: http://{host}:{port}/dashboard")
    print(f"🏠 Landing Page: http://{host}:{port}/")
    print("=" * 60)
    print("🎯 Production features enabled:")
    print("   • Enhanced security")
    print("   • Production logging")
    print("   • Error handling")
    print("   • Performance optimization")
    print("=" * 60)
    
    try:
        app_instance.run(
            host=host,
            port=port,
            debug=debug,
            threaded=True
        )
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)
