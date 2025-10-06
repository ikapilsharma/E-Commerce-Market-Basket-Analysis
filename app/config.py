import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database configuration - using your existing PostgreSQL database
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'mba_db')
    DB_USER = os.getenv('DB_USER', 'matth')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'Delaune.7467')
    DB_PORT = os.getenv('DB_PORT', '5432')
    
    # Flask configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'
    
    # API configuration
    API_TITLE = 'E-Commerce Market Basket Analysis API'
    API_VERSION = 'v1'

