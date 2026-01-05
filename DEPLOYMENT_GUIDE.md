# Production Deployment Guide

## College Management System - Deployment Instructions

This guide covers deploying the College Management System to a production environment.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Server Setup](#server-setup)
3. [Application Deployment](#application-deployment)
4. [Database Configuration](#database-configuration)
5. [Web Server Configuration](#web-server-configuration)
6. [Security Hardening](#security-hardening)
7. [Monitoring & Maintenance](#monitoring--maintenance)

---

## Prerequisites

### System Requirements
- **OS:** Ubuntu 20.04+ / CentOS 8+ / Windows Server 2019+
- **RAM:** Minimum 2GB, Recommended 4GB+
- **Disk:** 20GB+ free space
- **Python:** 3.10+
- **Database:** PostgreSQL 13+ (Recommended) or MySQL 8+

### Software Requirements
```bash
- Python 3.10+
- PostgreSQL/MySQL
- Nginx or Apache
- Git
- Gunicorn (WSGI server)
- Supervisor (Process manager)
```

---

## Server Setup

### 1. Update System
```bash
# Ubuntu/Debian
sudo apt update && sudo apt upgrade -y

# CentOS/RHEL
sudo yum update -y
```

### 2. Install Python and Dependencies
```bash
# Ubuntu
sudo apt install python3.10 python3-pip python3-venv -y

# CentOS
sudo yum install python3 python3-pip -y
```

### 3. Install PostgreSQL
```bash
# Ubuntu
sudo apt install postgresql postgresql-contrib -y

# CentOS
sudo yum install postgresql-server postgresql-contrib -y
sudo postgresql-setup initdb
```

### 4. Install Nginx
```bash
# Ubuntu
sudo apt install nginx -y

# CentOS
sudo yum install nginx -y
```

---

## Application Deployment

### 1. Create Application User
```bash
sudo adduser collegeapp
sudo usermod -aG sudo collegeapp
su - collegeapp
```

### 2. Clone Repository
```bash
cd /home/collegeapp
git clone https://github.com/yourusername/college-management-system.git
cd college-management-system
```

### 3. Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn psycopg2-binary
```

---

## Database Configuration

### 1. Create PostgreSQL Database
```bash
sudo -u postgres psql
```

```sql
CREATE DATABASE college_db;
CREATE USER college_user WITH PASSWORD 'strong_password_here';
ALTER ROLE college_user SET client_encoding TO 'utf8';
ALTER ROLE college_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE college_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE college_db TO college_user;
\q
```

### 2. Configure Database in Django

Create `.env` file:
```bash
nano .env
```

Add:
```env
DEBUG=False
SECRET_KEY=your-secret-key-here-min-50-characters-long
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com,your-server-ip

# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=college_db
DB_USER=college_user
DB_PASSWORD=strong_password_here
DB_HOST=localhost
DB_PORT=5432

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

# Security
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

### 3. Update Settings for Production

Edit `student_management_project/production_settings.py` or use environment variables.

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

---

## Web Server Configuration

### 1. Configure Gunicorn

Create Gunicorn socket:
```bash
sudo nano /etc/systemd/system/gunicorn.socket
```

Add:
```ini
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```

Create Gunicorn service:
```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Add:
```ini
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=collegeapp
Group=www-data
WorkingDirectory=/home/collegeapp/college-management-system
ExecStart=/home/collegeapp/college-management-system/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          student_management_project.wsgi:application

[Install]
WantedBy=multi-user.target
```

Start Gunicorn:
```bash
sudo systemctl start gunicorn.socket
sudo systemctl enable gunicorn.socket
```

### 2. Configure Nginx

Create Nginx configuration:
```bash
sudo nano /etc/nginx/sites-available/college
```

Add:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    client_max_body_size 20M;

    location = /favicon.ico { access_log off; log_not_found off; }
    
    location /static/ {
        alias /home/collegeapp/college-management-system/static/;
    }

    location /media/ {
        alias /home/collegeapp/college-management-system/media/;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $host;
        proxy_redirect off;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/college /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 3. Configure Firewall
```bash
sudo ufw allow 'Nginx Full'
sudo ufw enable
```

---

## SSL Certificate (HTTPS)

### Install Certbot
```bash
sudo apt install certbot python3-certbot-nginx -y
```

### Obtain Certificate
```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

### Auto-Renewal
Certbot automatically sets up renewal. Test it:
```bash
sudo certbot renew --dry-run
```

---

## Security Hardening

### 1. Django Settings

Ensure in `settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
```

### 2. Set File Permissions
```bash
cd /home/collegeapp/college-management-system
chmod -R 755 .
chmod 644 .env
chmod 600 db.sqlite3  # if using SQLite
```

### 3. Disable Root SSH Login
```bash
sudo nano /etc/ssh/sshd_config
```

Set:
```
PermitRootLogin no
PasswordAuthentication no
```

Restart SSH:
```bash
sudo systemctl restart sshd
```

### 4. Install Fail2Ban
```bash
sudo apt install fail2ban -y
sudo systemctl start fail2ban
sudo systemctl enable fail2ban
```

---

## Backup Configuration

### 1. Database Backup Script

Create backup script:
```bash
nano /home/collegeapp/backup_db.sh
```

Add:
```bash
#!/bin/bash
BACKUP_DIR="/home/collegeapp/backups"
DATE=$(date +%Y%m%d_%H%M%S)
DB_NAME="college_db"
DB_USER="college_user"

mkdir -p $BACKUP_DIR

# Backup database
PGPASSWORD="strong_password_here" pg_dump -U $DB_USER $DB_NAME > $BACKUP_DIR/db_$DATE.sql

# Keep only last 7 days backups
find $BACKUP_DIR -type f -mtime +7 -delete

echo "Backup completed: db_$DATE.sql"
```

Make executable:
```bash
chmod +x /home/collegeapp/backup_db.sh
```

### 2. Schedule with Cron
```bash
crontab -e
```

Add (daily at 2 AM):
```
0 2 * * * /home/collegeapp/backup_db.sh
```

---

## Monitoring & Maintenance

### 1. Check Gunicorn Status
```bash
sudo systemctl status gunicorn
```

### 2. Check Nginx Status
```bash
sudo systemctl status nginx
```

### 3. View Logs
```bash
# Gunicorn logs
sudo journalctl -u gunicorn

# Nginx access logs
sudo tail -f /var/log/nginx/access.log

# Nginx error logs
sudo tail -f /var/log/nginx/error.log

# Django logs
tail -f /home/collegeapp/college-management-system/logs/django.log
```

### 4. Restart Services
```bash
# Restart Gunicorn
sudo systemctl restart gunicorn

# Restart Nginx
sudo systemctl restart nginx

# Reload Nginx (graceful)
sudo systemctl reload nginx
```

### 5. Update Application
```bash
cd /home/collegeapp/college-management-system
source venv/bin/activate
git pull origin main
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn
```

---

## Performance Optimization

### 1. Enable Redis Caching
```bash
sudo apt install redis-server -y
```

Update settings:
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### 2. Configure Database Connection Pooling
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'CONN_MAX_AGE': 600,  # Connection pooling
        ...
    }
}
```

### 3. Enable Gzip Compression in Nginx
```nginx
gzip on;
gzip_types text/plain text/css application/json application/javascript;
gzip_min_length 1000;
```

---

## Troubleshooting

### Issue: 502 Bad Gateway
```bash
# Check if Gunicorn is running
sudo systemctl status gunicorn

# Check socket permissions
ls -l /run/gunicorn.sock

# Restart Gunicorn
sudo systemctl restart gunicorn
```

### Issue: Static Files Not Loading
```bash
# Recollect static files
python manage.py collectstatic --noinput

# Check Nginx configuration
sudo nginx -t

# Verify file permissions
ls -la /home/collegeapp/college-management-system/static/
```

### Issue: Database Connection Error
```bash
# Check PostgreSQL status
sudo systemctl status postgresql

# Test connection
psql -h localhost -U college_user -d college_db

# Check database settings in .env
```

---

## Post-Deployment Checklist

- [ ] Database is backed up automatically
- [ ] SSL certificate is installed
- [ ] DEBUG = False in production
- [ ] All static files are collected
- [ ] Email is configured and tested
- [ ] Firewall is enabled
- [ ] Monitoring is set up
- [ ] Logs are being recorded
- [ ] Error pages (404, 500) are configured
- [ ] Regular security updates scheduled

---

## Support

For deployment issues:
- Check logs first
- Review Django documentation
- Contact: devops@college.edu

---

**Deployment Guide Version:** 2.0.0  
**Last Updated:** January 5, 2026
