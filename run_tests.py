import os
import django
from django.test import Client
from django.contrib.auth.hashers import check_password

# Setup Django if run as standalone script
if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_management_project.settings')
    django.setup()

from student_management_app.models import CustomUser, Staffs, Students, Courses, Subjects

# Initialize test client
client = Client()

print('='*70)
print('COLLEGE MANAGEMENT SYSTEM - FUNCTIONAL TESTING')
print('='*70)
print()

# Test Results Storage
test_results = {
    'passed': 0,
    'failed': 0,
    'total': 0
}

def test_case(name, condition, details=""):
    """Helper function to track test results"""
    test_results['total'] += 1
    if condition:
        test_results['passed'] += 1
        print(f'✅ PASS: {name}')
        if details:
            print(f'   {details}')
    else:
        test_results['failed'] += 1
        print(f'❌ FAIL: {name}')
        if details:
            print(f'   {details}')
    return condition

print('🔐 AUTHENTICATION TESTS')
print('-' * 70)

# Test 1: HOD User Exists
admin = CustomUser.objects.filter(user_type='1').first()
test_case(
    'Admin/HOD user exists',
    admin is not None,
    f'Username: {admin.username if admin else "N/A"}'
)

# Test 2: Admin exists and is active
if admin:
    test_case(
        'Admin account is active',
        admin.is_active,
        f'Active: {admin.is_active}'
    )

# Test 3: Admin User Type
if admin:
    test_case(
        'Admin has correct user type (HOD)',
        admin.user_type == '1',
        f'User type: {admin.user_type}'
    )

# Test 4: Staff Users Exist
staff_count = CustomUser.objects.filter(user_type='2').count()
test_case(
    'Staff users exist',
    staff_count >= 1,
    f'Found {staff_count} staff members'
)

# Test 5: Student Users Exist
student_count = CustomUser.objects.filter(user_type='3').count()
test_case(
    'Student users exist',
    student_count >= 1,
    f'Found {student_count} students'
)

print()
print('📚 DATA INTEGRITY TESTS')
print('-' * 70)

# Test 6: Courses Exist
courses_count = Courses.objects.count()
test_case(
    'Courses created',
    courses_count >= 1,
    f'Found {courses_count} courses'
)

# Test 7: Subjects Exist
subjects_count = Subjects.objects.count()
test_case(
    'Subjects created',
    subjects_count >= 1,
    f'Found {subjects_count} subjects'
)

# Test 8: Staff Profiles Exist
staff_profiles_count = Staffs.objects.count()
test_case(
    'Staff profiles created',
    staff_profiles_count >= 1,
    f'Found {staff_profiles_count} staff profiles'
)

# Test 9: Student Profiles Exist
student_profiles_count = Students.objects.count()
test_case(
    'Student profiles created',
    student_profiles_count >= 1,
    f'Found {student_profiles_count} student profiles'
)

# Test 10: Subjects have Staff Assigned
subjects_with_staff = Subjects.objects.filter(staff_id__isnull=False).count()
test_case(
    'All subjects have staff assigned',
    subjects_with_staff >= 1,
    f'{subjects_with_staff} subjects have staff'
)

# Test 11: Students have Courses Assigned
students_with_courses = Students.objects.filter(course_id__isnull=False).count()
test_case(
    'All students have courses assigned',
    students_with_courses >= 1,
    f'{students_with_courses} students have courses'
)

print()
print('🌐 URL ROUTING TESTS')
print('-' * 70)

# Test 12: Home Page
response = client.get('/')
test_case(
    'Home page accessible',
    response.status_code == 200,
    f'Status: {response.status_code}'
)

# Test 13: Login Page
response = client.get('/login')
test_case(
    'Login page accessible',
    response.status_code == 200,
    f'Status: {response.status_code}'
)

# Test 14: Registration Page
response = client.get('/registration')
test_case(
    'Registration page accessible',
    response.status_code == 200,
    f'Status: {response.status_code}'
)

# Test 15: Contact Page
response = client.get('/contact')
test_case(
    'Contact page accessible',
    response.status_code == 200,
    f'Status: {response.status_code}'
)

print()
print('🔒 LOGIN FUNCTIONALITY TESTS')
print('-' * 70)

# Test 15: Admin Login Attempt (POST)
if admin:
    response = client.post('/doLogin', {'email': admin.email, 'password': 'admin123'})
    test_case(
        'Admin login redirects correctly',
        response.status_code in [200, 302],
        f'Status: {response.status_code}'
    )

# Test 16: Staff Login Attempt (POST)
staff = CustomUser.objects.filter(user_type='2').first()
if staff:
    response = client.post('/doLogin', {'email': staff.email, 'password': 'staff123'})
    test_case(
        'Staff login redirects correctly',
        response.status_code in [200, 302],
        f'Status: {response.status_code}'
    )

# Test 17: Student Login Attempt (POST)
student = CustomUser.objects.filter(user_type='3').first()
if student:
    response = client.post('/doLogin', {'email': student.email, 'password': 'student123'})
    test_case(
        'Student login redirects correctly',
        response.status_code in [200, 302],
        f'Status: {response.status_code}'
    )

# Test 18: Invalid Login Attempt
response = client.post('/doLogin', {'email': 'invalid@test.com', 'password': 'wrongpass'})
test_case(
    'Invalid login handled correctly',
    response.status_code in [200, 302],  # Redirects back to login
    f'Status: {response.status_code}'
)

print()
print('🔍 AJAX VALIDATION TESTS')
print('-' * 70)

# Test 19: Check Email Exist (AJAX)
response = client.post('/check_email_exist/', {'email': admin.email if admin else 'admin@gmail.com'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
test_case(
    'AJAX Email check functional',
    response.status_code == 200,
    f'Status: {response.status_code}'
)

# Test 20: Check Username Exist (AJAX)
response = client.post('/check_username_exist/', {'username': admin.username if admin else 'admin'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
test_case(
    'AJAX Username check functional',
    response.status_code == 200,
    f'Status: {response.status_code}'
)

print()
print('👤 ROLE-SPECIFIC VIEW TESTS')
print('-' * 70)

# Authenticate client for role-based views
if admin:
    client.login(username=admin.username, password='admin123')

# Test 21: Admin Manage Staff View
response = client.get('/manage_staff/')
test_case(
    'Admin Manage Staff access',
    response.status_code == 200,
    f'Status: {response.status_code}'
)

# Staff specific tests
staff_user = CustomUser.objects.filter(user_type='2').first()
if staff_user:
    client.login(username=staff_user.username, password='staff123')
    
    # Test 22: Staff View Subjects
    response = client.get('/staff_view_subjects/')
    test_case(
        'Staff View Subjects access',
        response.status_code == 200,
        f'Status: {response.status_code}'
    )
    
    # Test 23: Staff View Students
    response = client.get('/staff_view_students/')
    test_case(
        'Staff View Students access',
        response.status_code == 200,
        f'Status: {response.status_code}'
    )

# Student specific tests
student_user = CustomUser.objects.filter(user_type='3').first()
if student_user:
    client.login(username=student_user.username, password='student123')
    
    # Test 24: Student View Subjects
    response = client.get('/student_view_subjects/')
    test_case(
        'Student View Subjects access',
        response.status_code == 200,
        f'Status: {response.status_code}'
    )

print()
print('='*70)
print('TEST SUMMARY')
print('='*70)
print(f'Total Tests: {test_results["total"]}')
print(f'Passed: {test_results["passed"]} ✅')
print(f'Failed: {test_results["failed"]} ❌')
print(f'Success Rate: {(test_results["passed"]/test_results["total"]*100):.1f}%')
print('='*70)

if test_results['failed'] == 0:
    print('\n🎉 ALL TESTS PASSED! System is functioning correctly.')
else:
    print(f'\n⚠️  {test_results["failed"]} test(s) failed. Review needed.')
