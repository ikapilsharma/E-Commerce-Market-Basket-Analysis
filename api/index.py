"""
Vercel Serverless Function Entry Point
This file adapts the Flask application for Vercel's serverless architecture
"""
import sys
import os

# Add the app directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'app'))

# Import the Flask app
from app import app

# Vercel expects the app to be exported as 'app'
# This is the WSGI application that Vercel will run
handler = app

