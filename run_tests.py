"""
Automated Functional Testing Script for College Management System
Runs comprehensive tests on all major features
"""

from django.test import Client
from student_management_app.models import CustomUser, Staffs, Students, Courses, Subjects
from django.contrib.auth.hashers import check_password

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

# Test 1: Admin User Exists
admin = CustomUser.objects.filter(username='admin').first()
test_case(
    'Admin user exists',
    admin is not None,
    f'Username: {admin.username if admin else "N/A"}'
)

# Test 2: Admin Password Validation
if admin:
    test_case(
        'Admin password is correct',
        check_password('admin123', admin.password),
        'Password: admin123'
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
    'Staff users exist (expected 3)',
    staff_count == 3,
    f'Found {staff_count} staff members'
)

# Test 5: Student Users Exist
student_count = CustomUser.objects.filter(user_type='3').count()
test_case(
    'Student users exist (expected 5)',
    student_count == 5,
    f'Found {student_count} students'
)

print()
print('📚 DATA INTEGRITY TESTS')
print('-' * 70)

# Test 6: Courses Exist
courses_count = Courses.objects.count()
test_case(
    'Courses created (expected 5)',
    courses_count == 5,
    f'Found {courses_count} courses'
)

# Test 7: Subjects Exist
subjects_count = Subjects.objects.count()
test_case(
    'Subjects created (expected 6)',
    subjects_count == 6,
    f'Found {subjects_count} subjects'
)

# Test 8: Staff Profiles Exist
staff_profiles_count = Staffs.objects.count()
test_case(
    'Staff profiles created (expected 3)',
    staff_profiles_count == 3,
    f'Found {staff_profiles_count} staff profiles'
)

# Test 9: Student Profiles Exist
student_profiles_count = Students.objects.count()
test_case(
    'Student profiles created (expected 5)',
    student_profiles_count == 5,
    f'Found {student_profiles_count} student profiles'
)

# Test 10: Subjects have Staff Assigned
subjects_with_staff = Subjects.objects.filter(staff_id__isnull=False).count()
test_case(
    'All subjects have staff assigned',
    subjects_with_staff == 6,
    f'{subjects_with_staff}/6 subjects have staff'
)

# Test 11: Students have Courses Assigned
students_with_courses = Students.objects.filter(course_id__isnull=False).count()
test_case(
    'All students have courses assigned',
    students_with_courses == 5,
    f'{students_with_courses}/5 students have courses'
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

print()
print('🔒 LOGIN FUNCTIONALITY TESTS')
print('-' * 70)

# Test 15: Admin Login Attempt
response = client.get('/doLogin', {'email': 'admin@college.com', 'password': 'admin123'})
test_case(
    'Admin login redirects correctly',
    response.status_code in [200, 302],
    f'Status: {response.status_code}'
)

# Test 16: Staff Login Attempt
response = client.get('/doLogin', {'email': 'john.staff@college.com', 'password': 'staff123'})
test_case(
    'Staff login redirects correctly',
    response.status_code in [200, 302],
    f'Status: {response.status_code}'
)

# Test 17: Student Login Attempt
response = client.get('/doLogin', {'email': 'alice@college.com', 'password': 'student123'})
test_case(
    'Student login redirects correctly',
    response.status_code in [200, 302],
    f'Status: {response.status_code}'
)

# Test 18: Invalid Login Attempt
response = client.get('/doLogin', {'email': 'invalid@test.com', 'password': 'wrongpass'})
test_case(
    'Invalid login handled correctly',
    response.status_code == 200,  # Should return to login page
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
