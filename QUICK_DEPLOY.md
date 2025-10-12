# Quick Deployment Guide

## 🚨 Important Note

This Flask application with ML libraries (scikit-learn, mlxtend) may be **too large for Vercel's free tier** (50MB limit for serverless functions).

**Recommended Alternative Platforms:**
1. **Railway** ⭐ (Easiest, already configured)
2. **Render** ⭐ (Great free tier)
3. **Heroku** (Classic choice)
4. **DigitalOcean App Platform**

## Option 1: Deploy to Railway (Recommended) ⭐

Railway is **already configured** and perfect for this app!

### Steps:
```bash
# 1. Install Railway CLI
npm i -g railway

# 2. Login
railway login

# 3. Initialize (from project root)
cd /Users/kapilsharma/Downloads/E-Commerce-Marker-Basket-Analysis-main
railway init

# 4. Add PostgreSQL database
railway add postgresql

# 5. Deploy!
railway up

# 6. Get your URL
railway open
```

That's it! Railway will:
- ✅ Use your existing `Procfile`
- ✅ Use your existing `railway.json`
- ✅ Automatically provision PostgreSQL
- ✅ Set up environment variables
- ✅ Deploy in minutes

**Cost**: $5/month after free tier

---

## Option 2: Deploy to Render ⭐

### Steps:
1. Go to [render.com](https://render.com)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name**: ecommerce-analysis
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `cd app && gunicorn production_app:app`
5. Add a PostgreSQL database (free tier available)
6. Add environment variables from your `.env` file
7. Click **"Create Web Service"**

**Cost**: Free tier available!

---

## Option 3: Deploy to Vercel (Advanced)

⚠️ **May hit size limits** - Only try if you're on Vercel Pro or willing to troubleshoot.

### Quick Steps:
```bash
# 1. Install Vercel CLI
npm i -g vercel

# 2. Deploy
cd /Users/kapilsharma/Downloads/E-Commerce-Marker-Basket-Analysis-main
vercel

# 3. Add environment variables in Vercel dashboard
# 4. Deploy to production
vercel --prod
```

See `VERCEL_DEPLOYMENT.md` for detailed instructions.

---

## Option 4: Deploy to Heroku

### Steps:
```bash
# 1. Install Heroku CLI
brew tap heroku/brew && brew install heroku

# 2. Login
heroku login

# 3. Create app
heroku create your-app-name

# 4. Add PostgreSQL
heroku addons:create heroku-postgresql:mini

# 5. Deploy
git push heroku main

# 6. Scale dynos
heroku ps:scale web=1
```

---

## Environment Variables Needed

For all platforms, you need these environment variables:

```bash
SECRET_KEY=your-random-secret-key
FLASK_ENV=production
DB_HOST=your-db-host
DB_NAME=mba_db
DB_USER=your-db-user
DB_PASSWORD=your-db-password
DB_PORT=5432
```

---

## Database Setup

After deployment, populate your database:

```bash
# Option 1: From local machine
psql postgresql://user:pass@host/dbname < scripts/create_tables.sql

# Option 2: Use provider's web console
# Copy/paste the SQL from scripts/create_tables.sql
```

---

## Testing Deployment

After deployment, test these URLs:
- Landing: `https://your-app.com/`
- Dashboard: `https://your-app.com/dashboard`
- Advanced: `https://your-app.com/advanced-dashboard`
- API: `https://your-app.com/api/stats`

---

## Need Help?

1. **Railway Issues**: [docs.railway.app](https://docs.railway.app)
2. **Render Issues**: [render.com/docs](https://render.com/docs)
3. **Vercel Issues**: See `VERCEL_DEPLOYMENT.md`

## Comparison

| Platform | Free Tier | Setup | Best For |
|----------|-----------|-------|----------|
| **Railway** | $5 credit | ⭐⭐⭐⭐⭐ Easiest | This app! |
| **Render** | Yes | ⭐⭐⭐⭐ Easy | Free hosting |
| **Vercel** | Yes | ⭐⭐⭐ Medium | Serverless |
| **Heroku** | No | ⭐⭐⭐ Medium | Classic apps |

**Our Recommendation**: Start with **Railway** - it's the easiest and most reliable for this Flask + ML + PostgreSQL app!

