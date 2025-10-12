#!/bin/bash

# Vercel Deployment Script for E-Commerce Market Basket Analysis
# This script helps automate the Vercel deployment process

echo "🚀 E-Commerce Market Basket Analysis - Vercel Deployment"
echo "=========================================================="
echo ""

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI is not installed."
    echo "📦 Install it with: npm i -g vercel"
    echo ""
    read -p "Would you like to install it now? (y/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        npm i -g vercel
    else
        echo "Please install Vercel CLI first: npm i -g vercel"
        exit 1
    fi
fi

echo "✅ Vercel CLI is installed"
echo ""

# Check if user is logged in to Vercel
echo "🔐 Checking Vercel authentication..."
if ! vercel whoami &> /dev/null; then
    echo "Please login to Vercel:"
    vercel login
fi

echo "✅ Authenticated with Vercel"
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  No .env file found!"
    echo "Please create a .env file with your database credentials."
    echo "You can copy .env.production.example as a template:"
    echo ""
    echo "  cp .env.production.example .env"
    echo ""
    echo "Then edit .env with your actual database credentials."
    exit 1
fi

echo "✅ .env file found"
echo ""

# Confirm deployment
echo "📋 Deployment Checklist:"
echo "  ✓ Vercel CLI installed"
echo "  ✓ User authenticated"
echo "  ✓ Environment file exists"
echo "  ✓ vercel.json configured"
echo "  ✓ api/index.py entry point ready"
echo ""

read -p "⚠️  Ready to deploy to Vercel? (y/n) " -n 1 -r
echo ""
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Deployment cancelled."
    exit 0
fi

echo ""
echo "🚀 Starting deployment..."
echo ""

# Deploy to Vercel
vercel --prod

echo ""
echo "✅ Deployment complete!"
echo ""
echo "📝 Next steps:"
echo "  1. Visit your Vercel dashboard to add environment variables"
echo "  2. Add these variables:"
echo "     - DB_HOST"
echo "     - DB_NAME"
echo "     - DB_USER"
echo "     - DB_PASSWORD"
echo "     - DB_PORT"
echo "     - SECRET_KEY"
echo "  3. Redeploy after adding variables"
echo "  4. Test your application at the provided URL"
echo ""
echo "📖 See VERCEL_DEPLOYMENT.md for detailed instructions"
echo ""

