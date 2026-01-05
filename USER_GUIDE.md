# College Management System - User Guide

Welcome to the College Management System! This comprehensive guide will help you understand and use all features of the system based on your role.

## Table of Contents
- [Getting Started](#getting-started)
  - [Accessing the System](#accessing-the-system)
  - [Public Registration](#public-registration)
  - [Contact Page](#contact-page)
- [User Roles](#user-roles)
- [Admin/HOD Features](#adminhod-features)
- [Staff Features](#staff-features)
- [Student Features](#student-features)
- [Common Features](#common-features)
- [Tips and Best Practices](#tips-and-best-practices)

---

## Getting Started

### Accessing the System

1. Open your web browser
2. Navigate to: `http://127.0.0.1:8000/`
3. Click the **Login** button
4. Enter your credentials (email and password)

### First Time Login

- **Email Format**: The system uses email addresses as usernames
- **Password**: Use the password provided by your administrator or the one you set during registration

### Dashboard Overview

After logging in, you'll see your role-specific dashboard with:
- **Statistics Cards**: Quick overview of key metrics (Students, Staff, Courses, etc.)
- **Interactive Charts**: Real-time visual representation of data
- **Quick Actions**: Common tasks for your role (Add Student, Take Attendance, etc.)
- **Navigation Menu**: Side-bar access to all features

### Public Registration

If you don't have an account yet, you can register yourself:
1. Navigate to: `http://127.0.0.1:8000/registration`
2. Fill in the form:
   - **Full Name**: First and Last name
   - **Email Address**: Your primary contact email
   - **Password**: Secure password and confirmation
   - **Register As**: Choose between **Admin/HOD**, **Staff**, or **Student**
3. Click **Register**
4. Upon success, you can log in with your email and password.

### Contact Page

For pre-login inquiries or technical support:
1. Navigate to: `http://127.0.0.1:8000/contact`
2. View contact information and institutional details.

---

## User Roles

The system supports three user roles, each with specific permissions:

### 1. Admin/HOD (Head of Department)
- **Full system access**
- Manage all users (staff and students)
- Manage courses, subjects, and sessions
- View all reports and analytics
- System configuration

### 2. Staff
- Mark attendance for assigned subjects
- Enter and update student results
- Apply for leaves
- Send feedback to admin
- View assigned students and subjects

### 3. Student
- View attendance records
- View results/grades
- Apply for leaves
- Send feedback to admin
- Update profile information

---

## Admin/HOD Features

### Dashboard

The Admin dashboard provides comprehensive oversight with:

#### Statistics Overview
- **Total Students**: Number of enrolled students
- **Total Staff**: Number of staff members
- **Total Courses**: Available courses
- **Total Subjects**: Subjects offered

#### Interactive Charts
1. **Student Distribution by Course** (Pie Chart)
   - Visual breakdown of students per course
   - Color-coded for easy identification

2. **Subjects per Course** (Bar Chart)
   - Number of subjects in each course
   - Helps in curriculum planning

3. **Staff Attendance** (Stacked Bar Chart)
   - Classes attended vs Leaves taken per staff member
   - Identifies high leave usage or consistent attendance

4. **Student Attendance** (Grouped Bar Chart)
   - Classes attended vs Classes missed/leave per student
   - Identifies students requiring academic intervention

5. **Leave & Feedback Status** (Pie & Doughnut Charts)
   - Breakdown of Approved/Pending/Rejected leaves for both Students and Staff
   - Responsiveness overview for Student and Staff feedback (Replied vs Unreplied)

### 1. Student Management

#### Add New Student
1. Navigate to **Manage Students** → **Add Student**
2. Fill in the form:
   - **Email**: Must be unique (checked in real-time)
   - **Username**: Auto-generated from email (checked for uniqueness)
   - **Password**: Set initial password for the student
   - **First Name & Last Name**: Student's full name
   - **Address**: Physical address
   - **Course**: Select from available courses
   - **Session Year**: Academic year (Select from managed sessions)
   - **Gender**: Male/Female/Other
   - **Profile Picture** (Optional): Upload student photo
3. Click **Save**

#### View All Students
- Navigate to **Manage Students** → **View Students**
- See list of all enrolled students with:
  - Name and email
  - Course and session
  - Action buttons (Edit/Delete)

#### Edit Student Information
1. Click **Edit** button next to student name
2. Modify necessary fields
3. Click **Update**

#### Delete Student
- Click **Delete** button
- Confirm deletion (WARNING: This is permanent)

### 2. Staff Management

#### Add New Staff
1. Navigate to **Manage Staff** → **Add Staff**
2. Fill in the form:
   - **Email**: Must be unique (checked in real-time via AJAX)
   - **Password**: Set initial password
   - **First Name & Last Name**: Staff member's name
   - **Address**: Physical address
3. Click **Save**

#### View and Manage Staff
- View all staff members
- Edit staff information
- Delete staff accounts
- Assign subjects to staff

### 3. Course Management

#### Add New Course
1. Navigate to **Manage Courses** → **Add Course**
2. Enter:
   - **Course Name**: e.g., "Computer Science"
   - **Course Code** (if applicable)
3. Click **Save**

#### Edit/Delete Courses
- Modify course details
- Delete courses (WARNING: Affects associated students and subjects)

### 4. Subject Management

#### Add New Subject
1. Navigate to **Manage Subjects** → **Add Subject**
2. Fill in:
   - **Subject Name**: e.g., "Data Structures"
   - **Course**: Select the course this subject belongs to
   - **Staff**: Assign a teacher/instructor
3. Click **Save**

#### Manage Subjects
- Edit subject details
- Change assigned staff
- Delete subjects

### 5. Session Year Management

#### Create Session Year
1. Navigate to **Manage Sessions** → **Add Session**
2. Enter:
   - **Session Year**: e.g., "2024-2025"
   - **Start Date**: Academic year start
   - **End Date**: Academic year end
3. Click **Save**

### 6. Attendance Management

#### View Student Attendance
1. Navigate to **Attendance** → **View Attendance**
2. Filter by:
   - Course
   - Subject
   - Date range
3. View detailed attendance records

#### Attendance Reports
- Generate reports by student
- Generate reports by course
- Export data (if feature enabled)

### 7. Results Management

#### View All Results
1. Navigate to **Results** → **View Results**
2. Filter by:
   - Student
   - Course
   - Subject
   - Session year
3. View grades and performance

### 8. Leave Management

#### Review Leave Applications
1. Navigate to **Leave Requests**
2. See pending leave requests from staff and students
3. Actions:
   - **Approve**: Grant leave
   - **Reject**: Deny leave with reason
4. View leave history

### 9. Feedback Management

#### View Feedback
1. Navigate to **Feedback**
2. Read feedback from:
   - Staff members
   - Students
3. Take appropriate action based on feedback

### 10. System Settings

#### Update Profile
1. Click on your name in the top right
2. Select **Profile**
3. Update:
   - Profile picture
   - Contact information
   - Password

---

## Staff Features

### Dashboard

The Staff dashboard shows:

#### Statistics Cards
- **Students Count**: Number of students you teach
- **Subject Count**: Subjects assigned to you
- **Attendance Count**: Total attendance marked
- **Leave Count**: Your leave applications

#### Interactive Charts
1. **Attendance Overview** (Doughnut Chart)
   - Total attendance vs pending
   - Quick visual status

2. **Staff Statistics** (Bar Chart)
   - Visual summary of your assigned Students, Subjects, Attendance records, and Leaves.

### 1. View Assigned Data

#### View Your Subjects
1. Navigate to **Subjects** → **View Subjects**
2. See a list of all subjects specifically assigned to you by the Admin.

#### View Your Students
1. Navigate to **Students** → **View Students**
2. See a list of all students enrolled in the courses/subjects you teach.

### 2. Mark Attendance

#### Taking Attendance
1. Navigate to **Attendance** → **Take Attendance**
2. Select:
   - **Subject**: Choose from your assigned subjects
   - **Date**: Select attendance date
3. Mark each student as:
   - **Present** ✓
   - **Absent** ✗
4. Click **Submit Attendance**

#### Update Attendance
1. Navigate to **Attendance** → **Update Attendance**
2. Select the date and subject
3. Modify attendance records
4. Click **Update**

#### View Attendance
- See all attendance records you've marked
- Filter by date and subject
- Review attendance patterns

### 3. Student Results

#### Add Results
1. Navigate to **Results** → **Add Result**
2. Select:
   - **Student**: From your subject's students
   - **Subject**: Your assigned subject
   - **Exam Type**: Mid-term, Final, Quiz, etc.
3. Enter marks/grades
4. Click **Submit**

#### Update Results
1. Navigate to **Results** → **Update Result**
2. Select student and exam
3. Modify marks
4. Click **Update**

#### View Results History
1. Navigate to **Results** → **View Result**
2. See all results previously submitted for your subjects.

### 4. Leave Application

#### Apply for Leave
1. Navigate to **Leave** → **Apply Leave**
2. Fill in:
   - **Leave Date**: Date you need leave
   - **Reason**: Explain why you need leave
3. Click **Submit**
4. Wait for admin approval

#### View Leave Status
- Navigate to **Leave** → **View Leave**
- Check status: Pending, Approved, Rejected
- View leave history

### 5. Feedback

#### Send Feedback to Admin
1. Navigate to **Feedback** → **Send Feedback**
2. Write your message/concerns
3. Click **Submit**
4. Admin will review your feedback

### 6. Profile Management

#### Update Your Profile
1. Click your name → **Profile**
2. Update:
   - Profile picture
   - Contact information
   - Address
3. Click **Save**

---

## Student Features

### Dashboard

The Student dashboard displays:

#### Statistics Cards
- **Total Attendance**: Classes held
- **Present**: Classes attended
- **Absent**: Classes missed
- **Total Subjects**: Enrolled subjects

#### Visual Analytics
1. **Attendance Distribution** (Pie Chart)
   - Present vs Absent visualization
   - Easy to understand overview

2. **Attendance Percentage** (Large Display)
   - Color-coded percentage:
     - **Green** (≥75%): Excellent
     - **Yellow** (60-74%): Good, improve
     - **Red** (<60%): Below requirement
   - Animated progress bar
   - **Warning**: Displays a real-time warning message if your attendance is below 75%.

#### Quick Navigation
- **View My Attendance**: Direct link to your attendance logs.
- **View My Results**: Check your latest grades.
- **Apply for Leave**: Submit a leave request.
- **Send Feedback**: Message the administration.

#### Academic Summary
- Displays quick counts for Total Subjects, Classes Attended, and Classes Missed.

### 1. View Attendance

#### Check Your Attendance
1. Navigate to **Attendance** → **View Attendance**
2. See attendance records by:
   - Subject
   - Date
   - Status (Present/Absent)
3. Calculate your attendance percentage

#### Attendance Breakdown
- View subject-wise attendance
- Identify subjects needing more attention
- Track monthly attendance patterns

### 2. My Subjects

#### View Enrolled Subjects
1. Navigate to **Subjects** → **View Subjects**
2. See all subjects currently enrolled in for your course.

### 3. View Results

#### Check Your Grades
1. Navigate to **Results** → **View Results**
2. See grades for:
   - All subjects
   - Different exam types (Mid-term, Final, etc.)
   - Session-wise results
3. Track your academic performance

#### Grade Analysis
- View marks obtained vs total marks
- Calculate CGPA (if feature enabled)
- Compare performance across subjects

### 4. Apply for Leave

#### Submit Leave Application
1. Navigate to **Leave** → **Apply Leave**
2. Fill in:
   - **Leave Date**: Date you need leave
   - **Reason**: Valid reason (medical, personal, etc.)
   - **Supporting Documents** (if required)
3. Click **Submit**
4. Wait for approval

#### Check Leave Status
- View pending applications
- See approved/rejected leaves
- Check leave history

### 5. Send Feedback

#### Provide Feedback
1. Navigate to **Feedback** → **Send Feedback**
2. Write feedback about:
   - Teaching quality
   - System issues
   - Suggestions for improvement
3. Click **Submit**

### 6. Profile Management

#### Update Profile
1. Click your name → **Profile**
2. Update:
   - Profile picture
   - Contact information
   - Emergency contact (if available)
   - Password
3. Click **Save**

---

## Common Features

### 1. Logout

To safely logout:
1. Click **Logout** button in the top right
2. You'll be redirected to the login page
3. Your session will be cleared

### 2. Password Change

To change your password:
1. Go to **Profile**
2. Click **Change Password**
3. Enter:
   - Current password
   - New password
   - Confirm new password
4. Click **Update**

### 3. Navigation

#### Using the Sidebar Menu
- Click the menu icon (☰) to expand/collapse
- Navigate through different sections
- Current page is highlighted

#### Breadcrumb Navigation
- Shows your current location in the system
- Click on breadcrumb items to go back

### 4. Notifications

- Check for messages/alerts at the top
- Success messages (green): Operation successful
- Error messages (red): Action failed or details missing
- Warning messages (yellow): Important notices (e.g., low attendance)

---

## Tips and Best Practices

### For Admin/HOD

1. **Regular Backups**: Backup the database regularly
2. **Timely Updates**: Process leave requests promptly
3. **Data Verification**: Verify student and staff data accuracy
4. **Security**: Change default passwords immediately
5. **Monitoring**: Review attendance and feedback regularly

### For Staff

1. **Timely Attendance**: Mark attendance on time
2. **Accurate Results**: Double-check marks before submitting
3. **Clear Communication**: Provide detailed feedback
4. **Regular Updates**: Keep your profile information current
5. **Attendance Consistency**: Mark attendance daily

### For Students

1. **Regular Check-ins**: Check attendance and results weekly
2. **Maintain Attendance**: Aim for >75% attendance
3. **Timely Leave Applications**: Apply for leave in advance
4. **Constructive Feedback**: Provide helpful suggestions
5. **Profile Updates**: Keep contact information updated

### General Tips

1. **Use Strong Passwords**: Minimum 8 characters with mix of letters, numbers
2. **Logout After Use**: Always logout when done, especially on shared computers
3. **Report Issues**: Report bugs or problems to admin immediately
4. **Browser Compatibility**: Use modern browsers (Chrome, Firefox, Edge)
5. **Clear Cache**: Clear browser cache if you experience loading issues

---

## Keyboard Shortcuts

- **Ctrl + /**: Search (if enabled)
- **Ctrl + Home**: Go to dashboard
- **Esc**: Close modals/popups
- **Tab**: Navigate through form fields

---

## Mobile Access

The system is responsive and works on mobile devices:
- Access via mobile browser
- Navigation menu adapts to screen size
- Charts are optimized for mobile viewing
- Touch-friendly interface

---

## Frequently Asked Questions

### Q: I forgot my password. What should I do?
**A:** Contact your admin to reset your password.

### Q: Why can't I see all menu options?
**A:** Menu options depend on your role. Each role has access to specific features only.

### Q: My attendance percentage is wrong. How to fix it?
**A:** Contact your staff member or admin to verify and update attendance records.

### Q: Can I delete my account?
**A:** Only admins can delete accounts. Contact your admin if you need to remove your account.

### Q: How do I upload a profile picture?
**A:** Go to Profile → Click on profile picture area → Select file → Save.

### Q: Charts are not displaying. What's wrong?
**A:** Check your internet connection (Chart.js loads from CDN). Clear browser cache and reload the page.

### Q: Can I apply for leave for past dates?
**A:** This depends on system configuration. Usually, leave should be applied in advance.

---

## Troubleshooting

### Issue: Cannot login
- **Check**: Email format is correct
- **Verify**: Password is correct (case-sensitive)
- **Try**: Clear browser cookies and cache
- **Contact**: Admin if problem persists

### Issue: Page not loading
- **Check**: Internet connection
- **Try**: Refresh the page (F5 or Ctrl+R)
- **Clear**: Browser cache
- **Try**: Different browser

### Issue: Features not working
- **Check**: You have permission for that feature
- **Verify**: You're using the latest version
- **Contact**: Admin or technical support

---

## Support

For additional help:
- **Contact Admin**: Email your system administrator
- **Technical Issues**: Create an issue on GitHub
- **Documentation**: Refer to SETUP_GUIDE.md for installation help

---

## System Information

- **Version**: 2.0.0
- **Django Version**: 5.2.8
- **Python Version**: 3.8+
- **Last Updated**: January 5, 2026

---

**Thank you for using the College Management System!** 🎓

We hope this guide helps you make the most of the system. For suggestions or improvements, please send feedback through the system.
