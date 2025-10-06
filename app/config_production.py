import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class ProductionConfig:
    """Production configuration for E-Commerce Analytics Platform"""
    
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-production-secret-key-change-this')
    DEBUG = False
    TESTING = False
    
    # Database Configuration
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'mba_db')
    DB_USER = os.getenv('DB_USER', 'matth')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'your-db-password')
    DB_PORT = os.getenv('DB_PORT', '5432')
    
    # Application Configuration
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5003))
    
    # Security Configuration
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Performance Configuration
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    
    # Logging Configuration
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', 'app.log')

# Environment-specific configurations
config = {
    'development': {
        'DEBUG': True,
        'DB_HOST': 'localhost',
        'HOST': '127.0.0.1',
        'PORT': 5003
    },
    'production': ProductionConfig,
    'testing': {
        'DEBUG': True,
        'TESTING': True,
        'DB_NAME': 'test_mba_db'
    }
}
