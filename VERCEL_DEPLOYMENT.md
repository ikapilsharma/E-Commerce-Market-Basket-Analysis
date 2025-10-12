# Vercel Deployment Guide

This guide will help you deploy the E-Commerce Market Basket Analysis application to Vercel.

## Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **Vercel CLI** (optional): Install with `npm i -g vercel`
3. **PostgreSQL Database**: You'll need a cloud PostgreSQL database (recommended providers):
   - [Neon](https://neon.tech) - Free tier available
   - [Supabase](https://supabase.com) - Free tier available
   - [ElephantSQL](https://www.elephantsql.com) - Free tier available
   - [Railway](https://railway.app) - PostgreSQL hosting
   - [AWS RDS](https://aws.amazon.com/rds/)

## Important Notes

⚠️ **Vercel Limitations to Consider**:
- **Serverless Function Size**: Max 50MB (this app with ML libraries may exceed this)
- **Execution Time**: Max 10 seconds per request on Hobby plan (60s on Pro)
- **Memory**: 1024MB on Hobby, 3008MB on Pro
- **No Persistent Storage**: Use external database

💡 **Alternatives if Vercel doesn't work**:
- **Railway** (recommended for this app) - Better for Flask + PostgreSQL
- **Render** - Excellent free tier for Python apps
- **Heroku** - Classic PaaS solution
- **AWS Elastic Beanstalk** - Enterprise solution

## Step-by-Step Deployment

### 1. Setup Your Database

First, create a PostgreSQL database on one of the cloud providers mentioned above.

**For Neon (Recommended):**
1. Go to [neon.tech](https://neon.tech)
2. Sign up and create a new project
3. Copy your connection string (looks like: `postgresql://user:pass@host/dbname`)

### 2. Prepare Your Repository

Make sure your project is in a Git repository:

```bash
# Initialize git if not already done
cd /Users/kapilsharma/Downloads/E-Commerce-Marker-Basket-Analysis-main
git init
git add .
git commit -m "Initial commit for Vercel deployment"

# Push to GitHub (create a repo on GitHub first)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

### 3. Deploy to Vercel (Method 1: Web Dashboard)

1. Go to [vercel.com/dashboard](https://vercel.com/dashboard)
2. Click **"Add New..."** → **"Project"**
3. Import your GitHub repository
4. Configure the project:
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave as is)
   - **Build Command**: (leave empty)
   - **Output Directory**: (leave empty)

5. Add Environment Variables (click "Environment Variables"):
   ```
   DB_HOST=your-database-host.neon.tech
   DB_NAME=your_database_name
   DB_USER=your_database_user
   DB_PASSWORD=your_database_password
   DB_PORT=5432
   SECRET_KEY=your-secret-key-here-use-random-string
   FLASK_ENV=production
   ```

6. Click **"Deploy"**

### 4. Deploy to Vercel (Method 2: CLI)

```bash
# Login to Vercel
vercel login

# Deploy (from project root)
cd /Users/kapilsharma/Downloads/E-Commerce-Marker-Basket-Analysis-main
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? (choose your account)
# - Link to existing project? No
# - What's your project's name? ecommerce-market-basket-analysis
# - In which directory is your code located? ./

# Add environment variables
vercel env add DB_HOST
vercel env add DB_NAME
vercel env add DB_USER
vercel env add DB_PASSWORD
vercel env add DB_PORT
vercel env add SECRET_KEY

# Deploy to production
vercel --prod
```

### 5. Setup Database Schema

Once deployed, you need to populate your database with the schema and data.

**Option A: Use local script to connect to remote DB**
```bash
# Update your .env file with production database credentials
# Then run:
psql postgresql://user:pass@host/dbname < scripts/create_tables.sql
psql postgresql://user:pass@host/dbname < scripts/import_data.sql
```

**Option B: Use database provider's console**
- Most providers (Neon, Supabase) have a web-based SQL editor
- Copy and paste the contents of `scripts/create_tables.sql`
- Then import your data

### 6. Verify Deployment

After deployment completes:
1. Vercel will provide a URL (e.g., `https://your-project.vercel.app`)
2. Visit the URL to test:
   - Landing page: `https://your-project.vercel.app/`
   - Dashboard: `https://your-project.vercel.app/dashboard`
   - API: `https://your-project.vercel.app/api/stats`

## Troubleshooting

### Issue: Function Size Too Large

If you get "Function size exceeds the maximum" error:

**Solution 1**: Use Railway or Render instead (recommended)

**Solution 2**: Reduce dependencies
- Remove unused ML libraries from `requirements.txt`
- Use lighter alternatives

**Solution 3**: Upgrade to Vercel Pro
- Allows larger function sizes

### Issue: Database Connection Timeout

If database connections fail:

1. Check environment variables are set correctly
2. Ensure database allows external connections
3. Verify IP whitelisting (some providers require this)
4. Check if database is active (some free tiers pause after inactivity)

### Issue: Slow Response Times

Serverless functions have cold starts:
- First request may take 5-10 seconds
- Subsequent requests are faster
- Consider using Vercel Pro for better performance

### Issue: ML Models Too Heavy

If scikit-learn/mlxtend cause issues:

1. Consider pre-computing model results
2. Store results in database
3. Use lighter models
4. Deploy ML components separately

## Alternative: Deploy to Railway (Recommended)

Railway works better for this Flask + PostgreSQL + ML application:

```bash
# Install Railway CLI
npm i -g railway

# Login
railway login

# Initialize project
railway init

# Add PostgreSQL
railway add

# Deploy
railway up

# The Procfile and railway.json are already configured!
```

## Alternative: Deploy to Render

Render is also excellent for Python apps:

1. Go to [render.com](https://render.com)
2. Create a new Web Service
3. Connect your GitHub repository
4. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `cd app && gunicorn production_app:app`
5. Add environment variables (same as above)
6. Create a PostgreSQL database in Render
7. Deploy!

## Environment Variables Reference

Required environment variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `DB_HOST` | Database hostname | `ep-cool-name-123456.us-east-2.aws.neon.tech` |
| `DB_NAME` | Database name | `mba_db` |
| `DB_USER` | Database username | `your_username` |
| `DB_PASSWORD` | Database password | `your_secure_password` |
| `DB_PORT` | Database port | `5432` |
| `SECRET_KEY` | Flask secret key | `your-random-secret-key-here` |
| `FLASK_ENV` | Environment | `production` |

## Custom Domain (Optional)

To add a custom domain:
1. Go to your project settings in Vercel
2. Click "Domains"
3. Add your domain
4. Update DNS records as instructed

## Monitoring and Logs

- View logs: `vercel logs` or in Vercel dashboard
- Monitor performance in Vercel Analytics
- Set up error tracking (Sentry recommended)

## Cost Considerations

**Vercel Free Tier**:
- ✅ 100GB bandwidth
- ✅ Unlimited deployments
- ⚠️ Serverless function limitations
- ⚠️ 10s execution time

**Vercel Pro ($20/month)**:
- ✅ 1TB bandwidth
- ✅ Larger functions
- ✅ 60s execution time
- ✅ Better performance

**Recommendation**: Start with Railway or Render for this ML-heavy app, as they're better suited for non-serverless deployments.

## Support

If you encounter issues:
- Check Vercel documentation: [vercel.com/docs](https://vercel.com/docs)
- Railway documentation: [docs.railway.app](https://docs.railway.app)
- Render documentation: [render.com/docs](https://render.com/docs)

## Security Checklist

Before going to production:
- ✅ Set strong `SECRET_KEY`
- ✅ Use environment variables for all secrets
- ✅ Enable HTTPS (automatic on Vercel)
- ✅ Set up database backups
- ✅ Configure CORS properly
- ✅ Add rate limiting if needed
- ✅ Monitor logs for errors
- ✅ Set up error tracking

## Next Steps

After successful deployment:
1. Test all API endpoints
2. Verify data is loading correctly
3. Check dashboard visualizations
4. Monitor performance and errors
5. Set up automated backups
6. Configure monitoring/alerting

Good luck with your deployment! 🚀

