"""
WSGI entry point for Railway deployment
"""

import sys
import os

# Add the app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

# Import the Flask app
from app import app

# This is what Railway will run
application = app

if __name__ == "__main__":
    # For local testing
    port = int(os.environ.get('PORT', 5003))
    app.run(host='0.0.0.0', port=port, debug=False)
