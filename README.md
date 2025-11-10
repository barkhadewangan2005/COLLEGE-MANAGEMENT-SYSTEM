# 🎓 College Management System

A comprehensive, modern college management system built with Django 5.2.8 that streamlines academic administration with interactive dashboards, real-time analytics, and role-based access control.

![Django](https://img.shields.io/badge/Django-5.2.8-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

## ✨ Key Features

### 📊 Interactive Dashboards with Chart.js
- **Admin Dashboard**: 3 interactive charts (Student distribution, Subject analysis, Staff attendance)
- **Staff Dashboard**: 2 charts (Attendance overview, Statistics breakdown)
- **Student Dashboard**: Visual attendance tracking with color-coded percentage display

### 👥 Multi-User Role Management
- **Admin/HOD**: Complete system control, user management, analytics
- **Staff**: Attendance marking, result entry, leave management
- **Students**: View attendance/results, apply for leaves, provide feedback

### 📚 Comprehensive Academic Management
- **Student Management**: Enrollment, profile management, course assignment
- **Staff Management**: Teacher profiles, subject assignments
- **Course Management**: Course creation, curriculum organization
- **Subject Management**: Subject-to-course mapping, staff assignment
- **Session Management**: Academic year tracking

### 📅 Attendance System
- Real-time attendance marking by staff
- Attendance reports and analytics
- Subject-wise and date-wise filtering
- Automated percentage calculation with visual indicators
- Color-coded alerts (Green: ≥75%, Yellow: 60-74%, Red: <60%)

### 📝 Results Management
- Grade entry and updates by staff
- Result viewing for students
- Performance tracking and analytics
- Subject-wise grade reports

### 🏖️ Leave Management
- Leave application system for staff and students
- Admin approval workflow
- Leave status tracking (Pending/Approved/Rejected)
- Leave history records

### 💬 Feedback System
- Staff-to-admin feedback channel
- Student feedback submission
- Feedback tracking and review

### 🔐 Security & Authentication
- Django built-in authentication
- Role-based access control (RBAC)
- Password encryption
- Session management
- CSRF protection

### 🎨 Modern UI/UX
- AdminLTE 3.2 framework
- Bootstrap 4.6 responsive design
- Custom CSS with animations and gradients
- Mobile-friendly interface
- Hover effects and smooth transitions
- Accessibility improvements (ARIA labels, focus indicators)

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/barkhadewangan2005/COLLEGE-MANAGEMENT-SYSTEM.git
cd COLLEGE-MANAGEMENT-SYSTEM
```

2. **Create and activate virtual environment**

Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser (Admin)**
```bash
python manage.py createsuperuser
```
Follow the prompts to set up your admin account.

6. **Start development server**
```bash
python manage.py runserver
```

7. **Access the application**

Open your browser and navigate to: `http://127.0.0.1:8000/`

## 📖 Documentation

- **[SETUP_GUIDE.md](./SETUP_GUIDE.md)** - Detailed installation and configuration guide
- **[USER_GUIDE.md](./USER_GUIDE.md)** - Comprehensive user manual for all roles

## 👤 User Registration

The system automatically determines user roles based on email format:

- **Students**: `name.student@domain.com` (e.g., `john.student@college.com`)
- **Staff**: `name.staff@domain.com` (e.g., `jane.staff@college.com`)
- **Admin/HOD**: `name.hod@domain.com` (e.g., `admin.hod@college.com`)

New users can self-register through the registration page, or admins can create accounts directly.

## 💻 Technology Stack

### Backend
- **Python** 3.8+
- **Django** 5.2.8
- **SQLite3** (Database)

### Frontend
- **HTML5** / **CSS3**
- **JavaScript** / **jQuery** 3.6.0
- **Bootstrap** 4.6.0
- **AdminLTE** 3.2 (Admin Dashboard Theme)
- **Chart.js** 3.9.1 (Interactive Charts)
- **Font Awesome** 5.15.4 (Icons)

### Additional Libraries
- **Pillow** (Image Processing)
- Custom CSS with animations and responsive design

## 📁 Project Structure

```
COLLEGE-MANAGEMENT-SYSTEM/
├── manage.py
├── requirements.txt
├── README.md
├── SETUP_GUIDE.md
├── USER_GUIDE.md
├── db.sqlite3
├── static/
│   ├── css/
│   │   └── custom.css
│   └── admin/
├── media/
├── student_management_app/
│   ├── models.py
│   ├── views.py
│   ├── HodViews.py
│   ├── StaffViews.py
│   ├── StudentViews.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login_page.html
│   │   ├── registration.html
│   │   ├── hod_template/
│   │   ├── staff_template/
│   │   └── student_template/
│   └── migrations/
└── student_management_project/
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    └── asgi.py
```

## 🎯 Core Features by Role

### Admin/HOD Dashboard
- ✅ Interactive charts (Student distribution, Subject count, Staff attendance)
- ✅ Complete user management (Add/Edit/Delete staff and students)
- ✅ Course and subject administration
- ✅ Session year management
- ✅ Comprehensive attendance reports
- ✅ Leave request approval system
- ✅ Feedback review and management
- ✅ System-wide analytics

### Staff Dashboard
- ✅ Visual attendance and statistics charts
- ✅ Mark and update student attendance
- ✅ Enter and modify student results
- ✅ Apply for leaves with reason
- ✅ Send feedback to administration
- ✅ View assigned subjects and students
- ✅ Profile management

### Student Dashboard
- ✅ Visual attendance pie chart
- ✅ Color-coded attendance percentage (Green/Yellow/Red)
- ✅ Animated progress bars
- ✅ View detailed attendance records
- ✅ Check results and grades
- ✅ Apply for leaves
- ✅ Submit feedback
- ✅ Update profile and password

## 🔧 Configuration

### Database Settings

By default, the system uses SQLite. To use PostgreSQL or MySQL, update `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Email Configuration

For password reset and notifications, configure email in `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

## 🧪 Testing

Run the Django test suite:

```bash
python manage.py test
```

Check for any issues:

```bash
python manage.py check
```

## 🚀 Deployment

For production deployment:

1. Set `DEBUG = False` in `settings.py`
2. Configure `ALLOWED_HOSTS` with your domain
3. Use a production-grade database (PostgreSQL recommended)
4. Set up static file serving with Nginx/Apache
5. Use Gunicorn or uWSGI as WSGI server
6. Enable HTTPS with SSL certificate
7. Configure proper backup procedures

See [SETUP_GUIDE.md](./SETUP_GUIDE.md) for detailed deployment instructions.

## 📸 Screenshots

### Admin Dashboard
- Interactive charts showing student distribution and staff attendance
- Real-time statistics and analytics

### Staff Dashboard
- Attendance overview with doughnut charts
- Quick actions for common tasks

### Student Dashboard
- Visual attendance tracking with color-coded percentage
- Academic summary and quick links

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- **Barkha Dewangan** - [barkhadewangan2005](https://github.com/barkhadewangan2005)

## 🙏 Acknowledgments

- Django Software Foundation
- AdminLTE Template
- Chart.js Library
- Bootstrap Framework
- Font Awesome Icons

## 📞 Support

For support and queries:
- Create an issue on GitHub
- Contact: barkhadewangan2005@github.com

## 🔄 Version History

- **v1.0.0** (November 2025)
  - Initial release
  - Complete college management system
  - Interactive dashboards with Chart.js
  - Role-based access control
  - Attendance and results management
  - Leave and feedback systems
  - Mobile-responsive UI

## 🎓 About

This College Management System is designed to streamline academic administration for educational institutions. Built with Django and modern web technologies, it provides a comprehensive solution for managing students, staff, courses, attendance, and results with an intuitive, user-friendly interface.

---

**Made with ❤️ using Django**

For detailed documentation, please refer to:
- [SETUP_GUIDE.md](./SETUP_GUIDE.md) for installation instructions
- [USER_GUIDE.md](./USER_GUIDE.md) for feature documentation