# 🎓 College Management System - Manual Run Guide

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Step-by-Step Setup](#step-by-step-setup)
3. [Running the Application](#running-the-application)
4. [First-Time Setup](#first-time-setup)
5. [Troubleshooting](#troubleshooting)
6. [Common Commands](#common-commands)

---

## ✅ Prerequisites

Before you start, ensure you have:

- **Python 3.8 or higher** installed
- **pip** (Python package manager) - comes with Python
- **Git** (optional, for cloning the repository)
- A code editor or terminal (PowerShell, CMD, or Terminal)
- At least **500MB** free disk space
- Internet connection (to download dependencies)

### Check Python Installation:

```powershell
# Check Python version
python --version

# Check pip installation
pip --version
```

If these commands don't work, you need to:
1. Install Python from [python.org](https://www.python.org/downloads/)
2. Make sure to **check "Add Python to PATH"** during installation

---

## 🚀 Step-by-Step Setup

### **Step 1: Navigate to Project Directory**

```powershell
# Change to the project directory
cd D:\COLLEGE-MANAGEMENT-SYSTEM

# Or if it's elsewhere:
cd "C:\Users\YourUsername\Downloads\COLLEGE-MANAGEMENT-SYSTEM"
cd "/home/username/COLLEGE-MANAGEMENT-SYSTEM"  # Linux/Mac
```

### **Step 2: Create Virtual Environment**

A virtual environment keeps project dependencies isolated.

#### **Windows (PowerShell):**
```powershell
python -m venv venv
```

#### **Windows (CMD):**
```cmd
python -m venv venv
```

#### **macOS/Linux:**
```bash
python3 -m venv venv
```

**What this does:** Creates a folder named `venv` with isolated Python environment.

### **Step 3: Activate Virtual Environment**

#### **Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**Note:** If you get an error about execution policies, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try the activation command again.

#### **Windows (CMD):**
```cmd
venv\Scripts\activate.bat
```

#### **macOS/Linux:**
```bash
source venv/bin/activate
```

**Verify activation:** Your terminal should show `(venv)` at the beginning of the line.

```powershell
(venv) PS D:\COLLEGE-MANAGEMENT-SYSTEM>
```

### **Step 4: Install Dependencies**

```powershell
# Make sure you're in the project directory
cd D:\COLLEGE-MANAGEMENT-SYSTEM

# Install all required packages
pip install -r requirements.txt
```

This installs:
- **Django 5.2.8** - Web framework
- **Pillow** - Image processing
- **Django Debug Toolbar** - Development tools
- Other production dependencies

**Expected output:**
```
Successfully installed Django-5.2.8 Pillow-10.0.0 django-debug-toolbar-4.1.0 ...
```

### **Step 5: Apply Database Migrations**

Migrations set up the database structure.

```powershell
python manage.py migrate
```

**Expected output:**
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, student_management_app
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  ...
```

---

## ▶️ Running the Application

### **Step 6: Start the Development Server**

```powershell
python manage.py runserver
```

**Expected output:**
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 5, 2026 - 12:00:00
Django version 5.2.8, using settings 'student_management_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### **Step 7: Access the Application**

Open your web browser and go to:
```
http://127.0.0.1:8000/
```

You should see the College Management System home page.

---

## 🎯 First-Time Setup

### **Create an Admin/HOD Account**

1. Go to the registration page: `http://127.0.0.1:8000/registration`
2. Fill in the form:
   - **First Name:** Your first name
   - **Last Name:** Your last name
   - **Email:** Your email (Recommended format: `name.hod@college.com`)
   - **Password:** Your password
   - **Confirm Password:** Repeat the password
   - **Register As:** Select **Admin/HOD**
3. Click **Register**

### **Login to the System**

1. Go to login page: `http://127.0.0.1:8000/login`
2. Enter your email and password
3. Click **Login**
4. You'll be directed to the Admin/HOD Dashboard

### **Quick Setup Checklist**

After logging in as admin:

- [ ] Go to "Add Course" and add at least one course (e.g., "BCA", "MCA")
- [ ] Go to "Add Session Year" and add current academic year
- [ ] Go to "Add Staff" and add at least one staff member
- [ ] Go to "Add Student" and add a student (select the course you created)
- [ ] Test other features (Attendance, Results, etc.)

---

## 🔄 Subsequent Runs

Once you've completed the initial setup, for future runs:

```powershell
# 1. Navigate to project
cd D:\COLLEGE-MANAGEMENT-SYSTEM

# 2. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 3. Start server
python manage.py runserver
```

That's it! The application will start and be available at `http://127.0.0.1:8000/`

---

## 🛠️ Common Commands

### **Run Server on Different Port**
```powershell
python manage.py runserver 8080
```

### **Create Superuser (Admin via Django Admin)**
```powershell
python manage.py createsuperuser
```

### **Make Database Migrations** (if you modify models)
```powershell
python manage.py makemigrations
python manage.py migrate
```

### **Collect Static Files** (for production)
```powershell
python manage.py collectstatic --noinput
```

### **Check for Issues**
```powershell
python manage.py check
```

### **View All URLs**
```powershell
python manage.py show_urls
```

### **Clear Cache** (if needed)
```powershell
python manage.py clear_cache
```

### **Deactivate Virtual Environment**
```powershell
deactivate
```

---

## 🔓 Troubleshooting

### **Problem 1: Python not recognized**

**Error:** `'python' is not recognized as an internal or external command`

**Solutions:**
- Install Python from [python.org](https://www.python.org/downloads/)
- Add Python to PATH during installation
- Use full path: `C:\Python314\python.exe`

### **Problem 2: Cannot activate virtual environment**

**Error:** `cannot be loaded because running scripts is disabled on this system`

**Solution (PowerShell):**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then try activation again:
```powershell
.\venv\Scripts\Activate.ps1
```

### **Problem 3: Port 8000 already in use**

**Error:** `Error: That port is already in use.`

**Solutions:**
```powershell
# Use a different port
python manage.py runserver 8080

# Or kill the process using port 8000 (Windows)
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### **Problem 4: Module not found errors**

**Error:** `ModuleNotFoundError: No module named 'django'`

**Solutions:**
1. Make sure virtual environment is activated (check for `(venv)` prefix)
2. Reinstall dependencies:
   ```powershell
   pip install -r requirements.txt
   ```

### **Problem 5: Database errors**

**Error:** `django.db.utils.OperationalError`

**Solutions:**
```powershell
# Reset database (⚠️ This deletes all data!)
rm db.sqlite3

# Reapply migrations
python manage.py migrate

# Create sample data (if available)
python manage.py create_initial_data
```

### **Problem 6: Static files not loading**

**Symptoms:** CSS/images not displaying correctly

**Solutions:**
```powershell
# Create static directory if missing
mkdir student_management_app\static

# Collect static files
python manage.py collectstatic --noinput
```

---

## 📊 User Roles & Email Format

The system automatically assigns roles based on email format:

| Role | Email Format | Dashboard |
|------|-------------|-----------|
| **Admin/HOD** | `name.hod@domain.com` | Admin Panel |
| **Staff** | `name.staff@domain.com` | Staff Dashboard |
| **Student** | `name.student@domain.com` | Student Dashboard |

**Examples:**
```
admin.hod@college.com          → Admin role
john.staff@college.com          → Staff role
alice.student@college.com       → Student role
```

---

## 📁 Project Structure

```
COLLEGE-MANAGEMENT-SYSTEM/
├── venv/                              # Virtual environment (created by you)
│   ├── Scripts/
│   │   └── Activate.ps1             # Activation script
│   └── ...
├── student_management_project/       # Django project config
│   ├── settings.py                  # Main settings
│   ├── urls.py                      # URL routing
│   └── wsgi.py
├── student_management_app/          # Main app
│   ├── models.py                    # Database models
│   ├── views.py                     # Views
│   ├── HodViews.py                  # Admin views
│   ├── StaffViews.py                # Staff views
│   ├── StudentViews.py              # Student views
│   ├── templates/                   # HTML templates
│   ├── static/                      # CSS, JS, images
│   └── migrations/                  # Database migrations
├── static/                          # Collected static files
├── media/                           # User uploads
├── db.sqlite3                       # Database file
├── manage.py                        # Django management script
└── requirements.txt                 # Dependencies list
```

---

## 🔐 Important Notes

### **Development vs Production**

This setup is for **development only**.

For production, you need:
- Set `DEBUG = False` in settings.py
- Use a production database (PostgreSQL, MySQL)
- Use Gunicorn or uWSGI
- Configure HTTPS/SSL
- Set up proper authentication
- Use environment variables for secrets

### **Security**

- Never commit passwords or secrets to git
- Change `SECRET_KEY` for production
- Don't expose `DEBUG = True` in production
- Use HTTPS in production
- Regularly update dependencies

---

## 📞 Quick Reference

### **Windows PowerShell Commands:**

```powershell
# 1. Navigate to project
cd D:\COLLEGE-MANAGEMENT-SYSTEM

# 2. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 3. Install dependencies (first time only)
pip install -r requirements.txt

# 4. Apply migrations (first time only)
python manage.py migrate

# 5. Start server
python manage.py runserver

# 6. Open in browser
Start-Process http://127.0.0.1:8000/

# 7. Stop server (in terminal)
# Press CTRL+BREAK or CTRL+C
```

### **macOS/Linux Commands:**

```bash
# 1. Navigate to project
cd /path/to/COLLEGE-MANAGEMENT-SYSTEM

# 2. Activate virtual environment
source venv/bin/activate

# 3. Install dependencies (first time only)
pip install -r requirements.txt

# 4. Apply migrations (first time only)
python manage.py migrate

# 5. Start server
python manage.py runserver

# 6. Open in browser (macOS)
open http://127.0.0.1:8000/

# 7. Stop server
# Press CTRL+C
```

---

## ✅ Verification Checklist

After following this guide:

- [ ] Python installed and working
- [ ] Virtual environment created
- [ ] Virtual environment activated (showing `(venv)` in terminal)
- [ ] Dependencies installed successfully
- [ ] Migrations applied without errors
- [ ] Server running without errors
- [ ] Can access http://127.0.0.1:8000/ in browser
- [ ] Registration page loads
- [ ] Can create a new user account
- [ ] Can login successfully
- [ ] Dashboard loads after login

---

## 🎉 Success!

Once all steps are complete, you have a fully functional College Management System running locally!

**Happy managing! 🚀**

For more detailed information, see:
- README.md
- USER_GUIDE.md
- SETUP_GUIDE.md

