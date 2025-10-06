# 🚀 GitHub Deployment Guide - E-Commerce Analytics Platform

This guide will help you deploy your project directly from GitHub to cloud platforms.

## 📋 Prerequisites

- GitHub account
- Your project uploaded to GitHub
- Cloud platform account (Railway/Render/Heroku)

## 🎯 Step-by-Step Deployment

### Step 1: Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit changes
git commit -m "Initial commit: E-Commerce Analytics Platform"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

### Step 2: Deploy to Railway (Recommended)

1. **Go to Railway**: https://railway.app
2. **Sign up/Login** with GitHub
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your repository**
6. **Railway will auto-detect Python and deploy**

#### Railway Configuration:
- **Build Command**: `pip install -r app/requirements.txt`
- **Start Command**: `cd app && python cloud_app.py`
- **Port**: Railway will set `PORT` environment variable

#### Add PostgreSQL Database:
1. **In Railway dashboard**, click "New"
2. **Select "Database" → "PostgreSQL"**
3. **Railway will provide connection details**
4. **Add environment variables**:
   ```
   DB_HOST=<railway-provided-host>
   DB_NAME=<railway-provided-db-name>
   DB_USER=<railway-provided-user>
   DB_PASSWORD=<railway-provided-password>
   DB_PORT=<railway-provided-port>
   ```

### Step 3: Deploy to Render (Alternative)

1. **Go to Render**: https://render.com
2. **Sign up/Login** with GitHub
3. **Click "New +" → "Web Service"**
4. **Connect your GitHub repository**
5. **Configure**:
   - **Name**: `ecommerce-analytics`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r app/requirements.txt`
   - **Start Command**: `cd app && python cloud_app.py`

#### Add PostgreSQL:
1. **Click "New +" → "PostgreSQL"**
2. **Choose plan** (Free tier available)
3. **Note connection details**
4. **Add environment variables** in your web service

### Step 4: Deploy to Heroku (Alternative)

1. **Install Heroku CLI**: https://devcenter.heroku.com/articles/heroku-cli
2. **Login**: `heroku login`
3. **Create app**: `heroku create your-app-name`
4. **Add PostgreSQL**: `heroku addons:create heroku-postgresql:mini`
5. **Set environment variables**:
   ```bash
   heroku config:set SECRET_KEY=your-secret-key
   heroku config:set DB_HOST=$(heroku config:get DATABASE_URL)
   ```
6. **Deploy**: `git push heroku main`

## 🔧 Environment Variables Setup

### Required Variables:
```bash
SECRET_KEY=your-super-secret-key-change-this
FLASK_ENV=production
DB_HOST=your-database-host
DB_NAME=your-database-name
DB_USER=your-database-user
DB_PASSWORD=your-database-password
DB_PORT=5432
PORT=5003  # Will be set by cloud platform
```

### Setting Variables:

#### Railway:
1. **Go to your project dashboard**
2. **Click on your service**
3. **Go to "Variables" tab**
4. **Add each variable**

#### Render:
1. **Go to your web service**
2. **Click "Environment" tab**
3. **Add each variable**

#### Heroku:
```bash
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DB_HOST=your-db-host
# ... add all variables
```

## 📊 Database Setup

### Option 1: Use Cloud Database (Recommended)
- Railway/Render/Heroku provide managed PostgreSQL
- No additional setup needed
- Automatic backups included

### Option 2: Import Your Data
```bash
# Connect to cloud database
psql -h your-db-host -U your-db-user -d your-db-name

# Import your data
\i scripts/create_tables.sql
\i scripts/import_data.sql
```

## 🌐 Custom Domain Setup

### Railway:
1. **Go to project settings**
2. **Click "Domains"**
3. **Add your custom domain**
4. **Update DNS records**

### Render:
1. **Go to your service settings**
2. **Click "Custom Domains"**
3. **Add your domain**
4. **Follow DNS instructions**

## 🔍 Monitoring & Logs

### Railway:
- **Logs**: Available in dashboard
- **Metrics**: Built-in monitoring
- **Alerts**: Configurable

### Render:
- **Logs**: Available in service dashboard
- **Metrics**: Basic monitoring
- **Health checks**: Automatic

### Heroku:
```bash
# View logs
heroku logs --tail

# View metrics
heroku ps
```

## 🚨 Troubleshooting

### Common Issues:

#### Build Failures:
- Check `requirements.txt` for missing dependencies
- Ensure Python version compatibility
- Verify build commands

#### Database Connection Issues:
- Check environment variables
- Verify database is running
- Test connection string

#### Port Issues:
- Ensure app uses `os.getenv('PORT')`
- Cloud platforms set PORT automatically

### Debug Commands:

#### Railway:
```bash
# View build logs in dashboard
# Check environment variables
```

#### Render:
```bash
# View deployment logs
# Check service status
```

#### Heroku:
```bash
heroku logs --tail
heroku run python app/cloud_app.py
```

## 🎉 Success!

Once deployed, your application will be available at:
- **Railway**: `https://your-app-name.up.railway.app`
- **Render**: `https://your-app-name.onrender.com`
- **Heroku**: `https://your-app-name.herokuapp.com`

### Access Your Deployed App:
- **Landing Page**: `https://your-url.com/`
- **Executive Dashboard**: `https://your-url.com/advanced-dashboard`
- **Analytics Dashboard**: `https://your-url.com/dashboard`

## 🔄 Auto-Deployment

All platforms support auto-deployment:
- **Push to main branch** → **Automatic deployment**
- **Pull requests** → **Preview deployments**
- **Rollback** → **One-click revert**

Your E-Commerce Analytics Platform is now live on the cloud! 🚀
