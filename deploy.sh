#!/bin/bash

# E-Commerce Analytics Platform Deployment Script
# This script automates the deployment process

set -e  # Exit on any error

echo "🚀 Starting E-Commerce Analytics Platform Deployment"
echo "=================================================="

# Configuration
APP_NAME="ecommerce-analytics"
APP_DIR="/var/www/$APP_NAME"
SERVICE_USER="www-data"
PYTHON_VERSION="3.9"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    print_error "Please run as root (use sudo)"
    exit 1
fi

# Update system packages
print_status "Updating system packages..."
apt update && apt upgrade -y

# Install required system packages
print_status "Installing system dependencies..."
apt install -y python3 python3-pip python3-venv nginx postgresql postgresql-contrib git

# Create application directory
print_status "Creating application directory..."
mkdir -p $APP_DIR
chown $SERVICE_USER:$SERVICE_USER $APP_DIR

# Copy application files
print_status "Copying application files..."
cp -r . $APP_DIR/
chown -R $SERVICE_USER:$SERVICE_USER $APP_DIR

# Create virtual environment
print_status "Creating Python virtual environment..."
cd $APP_DIR
sudo -u $SERVICE_USER python3 -m venv venv
sudo -u $SERVICE_USER venv/bin/pip install --upgrade pip

# Install Python dependencies
print_status "Installing Python dependencies..."
sudo -u $SERVICE_USER venv/bin/pip install -r app/requirements.txt

# Setup environment variables
print_status "Setting up environment variables..."
if [ ! -f $APP_DIR/.env ]; then
    cp $APP_DIR/env_example.txt $APP_DIR/.env
    print_warning "Please update .env file with your actual configuration"
fi

# Setup PostgreSQL database
print_status "Setting up PostgreSQL database..."
sudo -u postgres psql -c "CREATE DATABASE mba_db;" 2>/dev/null || print_warning "Database might already exist"
sudo -u postgres psql -c "CREATE USER matth WITH PASSWORD 'your-password';" 2>/dev/null || print_warning "User might already exist"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE mba_db TO matth;" 2>/dev/null || print_warning "Privileges might already be granted"

# Setup systemd service
print_status "Setting up systemd service..."
cp $APP_DIR/ecommerce-analytics.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable ecommerce-analytics

# Setup Nginx
print_status "Setting up Nginx..."
cp $APP_DIR/nginx.conf /etc/nginx/sites-available/$APP_NAME
ln -sf /etc/nginx/sites-available/$APP_NAME /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default

# Test Nginx configuration
nginx -t

# Start services
print_status "Starting services..."
systemctl start ecommerce-analytics
systemctl restart nginx

# Enable services to start on boot
systemctl enable ecommerce-analytics
systemctl enable nginx

# Check service status
print_status "Checking service status..."
systemctl status ecommerce-analytics --no-pager

echo ""
echo "🎉 Deployment completed successfully!"
echo "======================================"
echo "🌐 Application URL: http://your-domain.com"
echo "📊 Executive Dashboard: http://your-domain.com/advanced-dashboard"
echo "📈 Analytics Dashboard: http://your-domain.com/dashboard"
echo "🏠 Landing Page: http://your-domain.com/advanced-dashboard"
echo ""
echo "📋 Next Steps:"
echo "1. Update /etc/nginx/sites-available/$APP_NAME with your domain"
echo "2. Update $APP_DIR/.env with your actual configuration"
echo "3. Setup SSL certificates for HTTPS"
echo "4. Import your database data"
echo ""
echo "🔧 Useful Commands:"
echo "• Check logs: journalctl -u ecommerce-analytics -f"
echo "• Restart app: systemctl restart ecommerce-analytics"
echo "• Check status: systemctl status ecommerce-analytics"
echo ""
