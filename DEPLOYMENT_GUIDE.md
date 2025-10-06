# 🚀 E-Commerce Analytics Platform - Deployment Guide

This guide provides multiple deployment options for your E-Commerce Market Basket Analysis project.

## 📋 Prerequisites

- Python 3.9+
- PostgreSQL 12+
- Git
- 2GB+ RAM
- 10GB+ Storage

## 🎯 Deployment Options

### Option 1: Local/VPS Deployment (Recommended)

#### Step 1: Prepare Your Server
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install -y python3 python3-pip python3-venv nginx postgresql postgresql-contrib git
```

#### Step 2: Run Deployment Script
```bash
# Clone your project
git clone <your-repo-url>
cd E-Commerce-Marker-Basket-Analysis-main

# Make deployment script executable
chmod +x deploy.sh

# Run deployment (as root)
sudo ./deploy.sh
```

#### Step 3: Configure Environment
```bash
# Edit environment variables
sudo nano /var/www/ecommerce-analytics/.env

# Update with your actual values:
# DB_PASSWORD=your-secure-password
# SECRET_KEY=your-super-secret-key
# HOST=0.0.0.0
# PORT=5003
```

#### Step 4: Setup Database
```bash
# Import your data
sudo -u postgres psql mba_db < scripts/create_tables.sql
sudo -u postgres psql mba_db < scripts/import_data.sql
```

#### Step 5: Configure Domain (Optional)
```bash
# Edit Nginx configuration
sudo nano /etc/nginx/sites-available/ecommerce-analytics

# Update server_name with your domain
# server_name your-domain.com www.your-domain.com;
```

### Option 2: Docker Deployment

#### Step 1: Install Docker & Docker Compose
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

#### Step 2: Deploy with Docker Compose
```bash
# Start all services
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

#### Step 3: Import Database Data
```bash
# Copy data files to containers
docker cp data/ ecommerce-analytics-db:/data/

# Import data
docker exec -it ecommerce-analytics-db psql -U matth -d mba_db -f /data/scripts/import_data.sql
```

### Option 3: Cloud Deployment

#### AWS EC2 Deployment
1. Launch EC2 instance (Ubuntu 20.04, t3.medium+)
2. Configure security groups (HTTP:80, HTTPS:443, SSH:22)
3. Follow Option 1 steps
4. Setup SSL with Let's Encrypt

#### Google Cloud Platform
1. Create Compute Engine instance
2. Configure firewall rules
3. Follow Option 1 steps
4. Setup Cloud Load Balancer

#### DigitalOcean Droplet
1. Create droplet (Ubuntu 20.04, 2GB RAM+)
2. Follow Option 1 steps
3. Setup SSL with Let's Encrypt

## 🔧 Configuration

### Environment Variables
```bash
# Required Variables
SECRET_KEY=your-super-secret-key-change-this
DB_HOST=localhost
DB_NAME=mba_db
DB_USER=matth
DB_PASSWORD=your-secure-password
DB_PORT=5432
HOST=0.0.0.0
PORT=5003
FLASK_ENV=production
```

### SSL Configuration
```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx

# Get SSL certificate
sudo certbot --nginx -d your-domain.com -d www.your-domain.com

# Auto-renewal
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

## 📊 Monitoring & Maintenance

### Health Checks
```bash
# Check application status
curl http://localhost:5003/api/stats

# Check service status
systemctl status ecommerce-analytics

# Check logs
journalctl -u ecommerce-analytics -f
```

### Performance Monitoring
```bash
# Monitor resources
htop
df -h
free -h

# Monitor application
tail -f /var/www/ecommerce-analytics/logs/app.log
```

### Backup Strategy
```bash
# Database backup
sudo -u postgres pg_dump mba_db > backup_$(date +%Y%m%d).sql

# Application backup
tar -czf app_backup_$(date +%Y%m%d).tar.gz /var/www/ecommerce-analytics
```

## 🚨 Troubleshooting

### Common Issues

#### Port Already in Use
```bash
# Find process using port 5003
sudo lsof -i :5003

# Kill process
sudo kill -9 <PID>
```

#### Database Connection Issues
```bash
# Check PostgreSQL status
sudo systemctl status postgresql

# Test connection
sudo -u postgres psql -c "SELECT version();"
```

#### Permission Issues
```bash
# Fix ownership
sudo chown -R www-data:www-data /var/www/ecommerce-analytics

# Fix permissions
sudo chmod -R 755 /var/www/ecommerce-analytics
```

### Log Locations
- Application logs: `/var/www/ecommerce-analytics/logs/app.log`
- System logs: `journalctl -u ecommerce-analytics`
- Nginx logs: `/var/log/nginx/`
- PostgreSQL logs: `/var/log/postgresql/`

## 🔒 Security Considerations

### Production Security Checklist
- [ ] Change default passwords
- [ ] Enable SSL/HTTPS
- [ ] Configure firewall
- [ ] Update system packages
- [ ] Use strong secret keys
- [ ] Enable database encryption
- [ ] Setup regular backups
- [ ] Monitor access logs

### Firewall Configuration
```bash
# Enable UFW
sudo ufw enable

# Allow SSH
sudo ufw allow ssh

# Allow HTTP/HTTPS
sudo ufw allow 80
sudo ufw allow 443

# Check status
sudo ufw status
```

## 📈 Scaling Considerations

### Horizontal Scaling
- Use load balancer (Nginx, HAProxy)
- Deploy multiple app instances
- Use Redis for session storage
- Implement database read replicas

### Vertical Scaling
- Increase server RAM
- Upgrade CPU cores
- Use SSD storage
- Optimize database queries

## 🎯 Performance Optimization

### Application Optimization
- Enable gzip compression
- Use CDN for static files
- Implement caching
- Optimize database queries

### Database Optimization
- Create proper indexes
- Regular VACUUM and ANALYZE
- Monitor query performance
- Use connection pooling

## 📞 Support

For deployment issues:
1. Check logs for error messages
2. Verify all services are running
3. Test database connectivity
4. Check firewall settings
5. Verify environment variables

## 🎉 Success!

Once deployed, your application will be available at:
- **Landing Page**: http://your-domain.com/
- **Executive Dashboard**: http://your-domain.com/advanced-dashboard
- **Analytics Dashboard**: http://your-domain.com/dashboard

Your E-Commerce Analytics Platform is now ready for production use! 🚀
