#!/bin/bash

# Railway Deployment Script
# Run this in your terminal where you're logged into Railway

echo "🚂 Railway Deployment Script"
echo "======================================="
echo ""

# Check if logged in
echo "Checking Railway authentication..."
if ! railway whoami &> /dev/null; then
    echo "❌ Not logged in to Railway!"
    echo "Please run: railway login"
    exit 1
fi

echo "✅ Logged in to Railway"
echo ""

# Project ID
PROJECT_ID="e51eb203-6ede-4117-877e-f2e248a76ef8"

echo "📦 Linking to your Railway project..."
railway link --project $PROJECT_ID

if [ $? -ne 0 ]; then
    echo "❌ Failed to link project"
    exit 1
fi

echo "✅ Project linked"
echo ""

# Check if PostgreSQL exists, if not, offer to add it
echo "🗄️  Checking for PostgreSQL..."
echo "If you don't have PostgreSQL yet, add it in Railway dashboard:"
echo "   1. Click '+ New'"
echo "   2. Select 'Database'"
echo "   3. Choose 'Add PostgreSQL'"
echo ""

# Set environment variables
echo "🔧 Setting environment variables..."
echo ""

# Generate a secure secret key
SECRET_KEY=$(openssl rand -hex 32)

railway variables set SECRET_KEY="$SECRET_KEY"
railway variables set FLASK_ENV="production"
railway variables set PORT="5003"

echo "✅ Environment variables set:"
echo "   - SECRET_KEY (generated)"
echo "   - FLASK_ENV=production"
echo "   - PORT=5003"
echo ""

# Deploy
echo "🚀 Deploying application..."
railway up

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Deployment successful!"
    echo ""
    echo "📊 Next steps:"
    echo "   1. Generate a domain: railway domain"
    echo "   2. Import database: railway run psql < scripts/create_tables.sql"
    echo "   3. View logs: railway logs"
    echo "   4. Open app: railway open"
    echo ""
else
    echo "❌ Deployment failed. Check the error messages above."
    exit 1
fi

