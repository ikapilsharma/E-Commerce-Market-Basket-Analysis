#!/bin/bash
cd /app
python -c "
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from app import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5003))
    host = os.environ.get('HOST', '0.0.0.0')
    print(f'🚀 Starting E-Commerce Market Basket Analysis on {host}:{port}')
    app.run(host=host, port=port, debug=False)
"
