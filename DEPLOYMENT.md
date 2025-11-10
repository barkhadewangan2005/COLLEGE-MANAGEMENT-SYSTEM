# College Management System - Deployment Guide

This guide provides detailed instructions for deploying the College Management System to production environments.

## Table of Contents
- [Pre-Deployment Checklist](#pre-deployment-checklist)
- [Production Settings](#production-settings)
- [Environment Variables](#environment-variables)
- [Database Setup](#database-setup)
- [Deployment Options](#deployment-options)
  - [Heroku Deployment](#heroku-deployment)
  - [AWS EC2 Deployment](#aws-ec2-deployment)
  - [DigitalOcean Deployment](#digitalocean-deployment)
  - [PythonAnywhere Deployment](#pythonanywhere-deployment)
- [Post-Deployment Steps](#post-deployment-steps)
- [Maintenance and Updates](#maintenance-and-updates)
- [Troubleshooting](#troubleshooting)

---

## Pre-Deployment Checklist

Before deploying to production, ensure you've completed these steps:

- [ ] All features tested and working in development
- [ ] Database migrations created and tested
- [ ] Static files collected and tested
- [ ] Environment variables configured
- [ ] Production settings file reviewed
- [ ] Secret key generated (new, never used before)
- [ ] Debug mode disabled (`DEBUG = False`)
- [ ] Allowed hosts configured
- [ ] Database backups configured
- [ ] SSL certificate obtained (for HTTPS)
- [ ] Email configuration tested
- [ ] Error logging configured
- [ ] Security checklist completed

### Run Django Security Check

```bash
python manage.py check --deploy
```

This command will identify potential security issues in your configuration.

---

## Production Settings

The project includes a `settings_production.py` file with production-ready configurations.

### Key Production Settings

1. **SECRET_KEY**: Must be unique and kept secret
2. **DEBUG**: Set to `False`
3. **ALLOWED_HOSTS**: List of allowed domain names
4. **Database**: PostgreSQL recommended (not SQLite)
5. **Static Files**: Configured with WhiteNoise
6. **Security Headers**: HSTS, SSL redirect, secure cookies enabled
7. **Logging**: Error and info logging to file and console

### Using Production Settings

Set the environment variable:

```bash
export DJANGO_SETTINGS_MODULE=student_management_project.settings_production
```

Or in Windows:
```powershell
$env:DJANGO_SETTINGS_MODULE="student_management_project.settings_production"
```

---

## Environment Variables

### Step 1: Copy Environment Template

```bash
cp .env.example .env
```

### Step 2: Generate Secret Key

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Copy the output and add it to your `.env` file.

### Step 3: Configure Environment Variables

Edit `.env` file with your production values:

```env
DJANGO_SECRET_KEY=your-generated-secret-key-here
DJANGO_SETTINGS_MODULE=student_management_project.settings_production
DJANGO_ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

DB_NAME=college_management_db
DB_USER=your_db_user
DB_PASSWORD=strong_password_here
DB_HOST=localhost
DB_PORT=5432

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

**Important**: Never commit `.env` file to version control!

---

## Database Setup

### PostgreSQL (Recommended)

#### 1. Install PostgreSQL

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

**macOS:**
```bash
brew install postgresql
```

**Windows:**
Download from https://www.postgresql.org/download/windows/

#### 2. Create Database and User

```bash
sudo -u postgres psql

CREATE DATABASE college_management_db;
CREATE USER your_db_user WITH PASSWORD 'your_strong_password';
ALTER ROLE your_db_user SET client_encoding TO 'utf8';
ALTER ROLE your_db_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE your_db_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE college_management_db TO your_db_user;
\q
```

#### 3. Install Python PostgreSQL Adapter

```bash
pip install psycopg2-binary
```

#### 4. Update requirements.txt

```bash
pip freeze > requirements.txt
```

#### 5. Run Migrations

```bash
python manage.py migrate
```

---

## Deployment Options

### Heroku Deployment

#### Prerequisites
- Heroku account
- Heroku CLI installed

#### Step 1: Install Required Packages

```bash
pip install gunicorn whitenoise psycopg2-binary dj-database-url
pip freeze > requirements.txt
```

#### Step 2: Create Procfile

Create `Procfile` in project root:

```
web: gunicorn student_management_project.wsgi --log-file -
```

#### Step 3: Create runtime.txt

```
python-3.11.0
```

#### Step 4: Update settings_production.py

Add at the top:

```python
import dj_database_url

# Add this after DATABASES configuration
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
```

#### Step 5: Login to Heroku

```bash
heroku login
```

#### Step 6: Create Heroku App

```bash
heroku create your-college-app-name
```

#### Step 7: Set Environment Variables

```bash
heroku config:set DJANGO_SECRET_KEY='your-secret-key'
heroku config:set DJANGO_SETTINGS_MODULE=student_management_project.settings_production
heroku config:set DJANGO_ALLOWED_HOSTS='your-app.herokuapp.com'
```

#### Step 8: Add PostgreSQL Database

```bash
heroku addons:create heroku-postgresql:hobby-dev
```

#### Step 9: Deploy

```bash
git add .
git commit -m "Prepare for Heroku deployment"
git push heroku main
```

#### Step 10: Run Migrations

```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

#### Step 11: Collect Static Files

```bash
heroku run python manage.py collectstatic --noinput
```

---

### AWS EC2 Deployment

#### Prerequisites
- AWS account
- EC2 instance (Ubuntu recommended)
- Elastic IP assigned
- Security group configured (ports 22, 80, 443)

#### Step 1: Connect to EC2

```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

#### Step 2: Update System

```bash
sudo apt update
sudo apt upgrade -y
```

#### Step 3: Install Dependencies

```bash
sudo apt install python3-pip python3-venv nginx postgresql postgresql-contrib -y
```

#### Step 4: Create Project Directory

```bash
cd /var/www
sudo mkdir college_management
sudo chown $USER:$USER college_management
cd college_management
```

#### Step 5: Clone Repository

```bash
git clone https://github.com/barkhadewangan2005/COLLEGE-MANAGEMENT-SYSTEM.git
cd COLLEGE-MANAGEMENT-SYSTEM
```

#### Step 6: Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install gunicorn
```

#### Step 7: Configure Environment Variables

```bash
cp .env.example .env
nano .env
# Edit with your production values
```

#### Step 8: Setup Database

Follow PostgreSQL setup steps above.

#### Step 9: Run Migrations

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

#### Step 10: Configure Gunicorn

Create `/etc/systemd/system/gunicorn.service`:

```ini
[Unit]
Description=gunicorn daemon for College Management System
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/var/www/college_management/COLLEGE-MANAGEMENT-SYSTEM
EnvironmentFile=/var/www/college_management/COLLEGE-MANAGEMENT-SYSTEM/.env
ExecStart=/var/www/college_management/COLLEGE-MANAGEMENT-SYSTEM/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/var/www/college_management/COLLEGE-MANAGEMENT-SYSTEM/gunicorn.sock \
          student_management_project.wsgi:application

[Install]
WantedBy=multi-user.target
```

#### Step 11: Start Gunicorn

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
sudo systemctl status gunicorn
```

#### Step 12: Configure Nginx

Create `/etc/nginx/sites-available/college_management`:

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        alias /var/www/college_management/COLLEGE-MANAGEMENT-SYSTEM/staticfiles/;
    }
    
    location /media/ {
        alias /var/www/college_management/COLLEGE-MANAGEMENT-SYSTEM/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/college_management/COLLEGE-MANAGEMENT-SYSTEM/gunicorn.sock;
    }
}
```

#### Step 13: Enable Site

```bash
sudo ln -s /etc/nginx/sites-available/college_management /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

#### Step 14: Setup SSL with Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

---

### DigitalOcean Deployment

Similar to AWS EC2 deployment, but use DigitalOcean Droplet instead.

#### Quick Start

1. Create Ubuntu Droplet
2. Follow AWS EC2 steps above
3. Point your domain to Droplet IP
4. Configure SSL with Let's Encrypt

---

### PythonAnywhere Deployment

#### Step 1: Create Account

Sign up at https://www.pythonanywhere.com

#### Step 2: Open Bash Console

```bash
git clone https://github.com/barkhadewangan2005/COLLEGE-MANAGEMENT-SYSTEM.git
cd COLLEGE-MANAGEMENT-SYSTEM
```

#### Step 3: Create Virtual Environment

```bash
mkvirtualenv --python=/usr/bin/python3.10 college_env
pip install -r requirements.txt
```

#### Step 4: Configure Web App

1. Go to Web tab
2. Add new web app
3. Choose Manual Configuration
4. Set Python version
5. Set virtualenv path: `/home/yourusername/.virtualenvs/college_env`
6. Edit WSGI file:

```python
import sys
import os

path = '/home/yourusername/COLLEGE-MANAGEMENT-SYSTEM'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'student_management_project.settings_production'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

#### Step 5: Set Environment Variables

In Web tab, add environment variables in .env file or PythonAnywhere settings.

#### Step 6: Configure Static Files

- URL: /static/
- Directory: /home/yourusername/COLLEGE-MANAGEMENT-SYSTEM/staticfiles/

#### Step 7: Run Commands

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

#### Step 8: Reload Web App

Click "Reload" button in Web tab.

---

## Post-Deployment Steps

### 1. Verify Deployment

- [ ] Homepage loads correctly
- [ ] Login works
- [ ] Static files load (CSS, JS, images)
- [ ] Admin panel accessible
- [ ] Database connections work
- [ ] Email sending works
- [ ] HTTPS enabled

### 2. Create Superuser (if not done)

```bash
python manage.py createsuperuser
```

### 3. Add Sample Data

Login as admin and create:
- Session years
- Courses
- Subjects
- Staff members
- Students

### 4. Test All Features

- User registration
- Login/logout
- Attendance marking
- Results entry
- Leave applications
- Feedback submission

### 5. Setup Monitoring

Consider using:
- **Sentry** for error tracking
- **New Relic** for performance monitoring
- **Uptime Robot** for uptime monitoring

### 6. Setup Backups

#### Database Backup Script

Create `backup_db.sh`:

```bash
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/var/backups/college_management"
mkdir -p $BACKUP_DIR

pg_dump -U your_db_user college_management_db > $BACKUP_DIR/db_backup_$DATE.sql

# Keep only last 7 days of backups
find $BACKUP_DIR -name "db_backup_*.sql" -mtime +7 -delete
```

Make executable:
```bash
chmod +x backup_db.sh
```

Add to crontab (daily at 2 AM):
```bash
crontab -e
# Add: 0 2 * * * /path/to/backup_db.sh
```

---

## Maintenance and Updates

### Updating Code

```bash
cd /path/to/project
git pull origin main
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn
sudo systemctl restart nginx
```

### Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Clear Cache (if using cache)

```bash
python manage.py clear_cache
```

---

## Troubleshooting

### Issue: Static Files Not Loading

**Solution:**
```bash
python manage.py collectstatic --noinput
sudo systemctl restart nginx
```

### Issue: 502 Bad Gateway

**Check Gunicorn:**
```bash
sudo systemctl status gunicorn
sudo journalctl -u gunicorn
```

### Issue: Database Connection Error

**Check PostgreSQL:**
```bash
sudo systemctl status postgresql
sudo -u postgres psql
```

### Issue: Permission Denied

**Fix permissions:**
```bash
sudo chown -R www-data:www-data /path/to/project
sudo chmod -R 755 /path/to/project
```

### View Logs

```bash
# Nginx logs
sudo tail -f /var/log/nginx/error.log

# Gunicorn logs
sudo journalctl -u gunicorn -f

# Django logs
tail -f /path/to/project/logs/django_errors.log
```

---

## Security Best Practices

1. **Always use HTTPS** in production
2. **Never commit** `.env` or `SECRET_KEY`
3. **Use strong passwords** for database and admin
4. **Keep dependencies updated** regularly
5. **Enable firewall** (UFW on Ubuntu)
6. **Restrict SSH** access (key-based only)
7. **Regular backups** of database and media files
8. **Monitor logs** for suspicious activity
9. **Use Django security checklist**: `python manage.py check --deploy`
10. **Implement rate limiting** for login attempts

---

## Support

For deployment issues:
- Check Django deployment docs: https://docs.djangoproject.com/en/5.2/howto/deployment/
- Create issue on GitHub: https://github.com/barkhadewangan2005/COLLEGE-MANAGEMENT-SYSTEM/issues
- Contact: barkhadewangan2005@github.com

---

**Version:** 1.0.0  
**Last Updated:** November 11, 2025  
**Django Version:** 5.2.8
