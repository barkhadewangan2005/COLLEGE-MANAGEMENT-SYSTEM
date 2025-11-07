# College Management System

A comprehensive college management system built with Django that helps manage students, staff, and administrative tasks.

## Features

- Multi-user roles (HOD/Admin, Staff, Student)
- Student Management
- Staff Management
- Course Management
- Subject Management
- Attendance Management
- Leave Management
- Feedback System
- User Authentication
- Profile Management

## Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/barkhadewangan2005/COLLEGE-MANAGEMENT-SYSTEM.git
cd COLLEGE-MANAGEMENT-SYSTEM
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create a superuser
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

## User Types and Registration

- Student: Use email format "name.student@college.com"
- Staff: Use email format "name.staff@college.com"
- HOD/Admin: Use email format "name.hod@college.com"

## Technology Stack

- Python
- Django
- SQLite3
- HTML/CSS
- Bootstrap
- JavaScript/jQuery