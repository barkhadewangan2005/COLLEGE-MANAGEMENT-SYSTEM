from django.core.management.base import BaseCommand
from student_management_app.models import (
    CustomUser, Courses, SessionYearModel, Staffs, Students, Subjects
)
from datetime import date

class Command(BaseCommand):
    help = 'Creates comprehensive sample data for testing the College Management System'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('\n' + '='*60))
        self.stdout.write(self.style.SUCCESS('CREATING SAMPLE DATA FOR COLLEGE MANAGEMENT SYSTEM'))
        self.stdout.write(self.style.SUCCESS('='*60 + '\n'))

        # Create Courses
        self.stdout.write(self.style.WARNING('📚 Creating Courses...'))
        courses_data = [
            'BCA - Bachelor of Computer Applications',
            'MCA - Master of Computer Applications',
            'B.Tech - Computer Science',
            'MBA - Business Administration'
        ]
        
        courses = []
        for course_name in courses_data:
            course, created = Courses.objects.get_or_create(course_name=course_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Created: {course_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'  ⚠ Already exists: {course_name}'))
            courses.append(course)

        # Create Session Years
        self.stdout.write(self.style.WARNING('\n📅 Creating Session Years...'))
        sessions_data = [
            (date(2024, 1, 1), date(2024, 12, 31)),
            (date(2025, 1, 1), date(2025, 12, 31)),
        ]
        
        sessions = []
        for start, end in sessions_data:
            session, created = SessionYearModel.objects.get_or_create(
                session_start_year=start,
                session_end_year=end
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Created: {start.year} - {end.year}'))
            else:
                self.stdout.write(self.style.WARNING(f'  ⚠ Already exists: {start.year} - {end.year}'))
            sessions.append(session)

        # Create Staff Members
        self.stdout.write(self.style.WARNING('\n👨‍🏫 Creating Staff Members...'))
        staff_data = [
            {
                'username': 'john_staff',
                'email': 'john.staff@college.com',
                'password': 'staff123',
                'first_name': 'John',
                'last_name': 'Doe',
                'address': '123 Staff Street, Education City'
            },
            {
                'username': 'jane_staff',
                'email': 'jane.staff@college.com',
                'password': 'staff123',
                'first_name': 'Jane',
                'last_name': 'Smith',
                'address': '456 Teacher Avenue, Knowledge Town'
            },
            {
                'username': 'mike_staff',
                'email': 'mike.staff@college.com',
                'password': 'staff123',
                'first_name': 'Mike',
                'last_name': 'Johnson',
                'address': '789 Faculty Road, Learning District'
            }
        ]

        staff_users = []
        for staff_info in staff_data:
            if not CustomUser.objects.filter(username=staff_info['username']).exists():
                user = CustomUser.objects.create_user(
                    username=staff_info['username'],
                    email=staff_info['email'],
                    password=staff_info['password'],
                    first_name=staff_info['first_name'],
                    last_name=staff_info['last_name'],
                    user_type='2'  # Staff
                )
                staff = Staffs.objects.create(
                    admin=user,
                    address=staff_info['address']
                )
                staff_users.append(staff)
                self.stdout.write(self.style.SUCCESS(
                    f'  ✓ Created: {staff_info["first_name"]} {staff_info["last_name"]} '
                    f'({staff_info["email"]})'
                ))
            else:
                user = CustomUser.objects.get(username=staff_info['username'])
                staff = Staffs.objects.get(admin=user)
                staff_users.append(staff)
                self.stdout.write(self.style.WARNING(
                    f'  ⚠ Already exists: {staff_info["first_name"]} {staff_info["last_name"]}'
                ))

        # Create Subjects
        self.stdout.write(self.style.WARNING('\n📖 Creating Subjects...'))
        subjects_data = [
            ('Data Structures', courses[0], staff_users[0]),  # BCA - John
            ('Database Management', courses[0], staff_users[1]),  # BCA - Jane
            ('Web Development', courses[1], staff_users[0]),  # MCA - John
            ('Machine Learning', courses[1], staff_users[2]),  # MCA - Mike
            ('Operating Systems', courses[2], staff_users[1]),  # B.Tech - Jane
            ('Business Management', courses[3], staff_users[2]),  # MBA - Mike
        ]

        for subject_name, course, staff in subjects_data:
            subject, created = Subjects.objects.get_or_create(
                subject_name=subject_name,
                course_id=course,
                staff_id=staff.admin  # Use the CustomUser instance from staff
            )
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f'  ✓ Created: {subject_name} ({course.course_name}) - '
                    f'Staff: {staff.admin.first_name} {staff.admin.last_name}'
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f'  ⚠ Already exists: {subject_name}'
                ))

        # Create Students
        self.stdout.write(self.style.WARNING('\n👨‍🎓 Creating Students...'))
        students_data = [
            {
                'username': 'alice_student',
                'email': 'alice@college.com',
                'password': 'student123',
                'first_name': 'Alice',
                'last_name': 'Brown',
                'address': '100 Student Lane, Campus Area',
                'course': courses[0],  # BCA
                'session': sessions[0],
                'gender': 'Female'
            },
            {
                'username': 'bob_student',
                'email': 'bob@college.com',
                'password': 'student123',
                'first_name': 'Bob',
                'last_name': 'Wilson',
                'address': '200 Dorm Street, Campus Area',
                'course': courses[0],  # BCA
                'session': sessions[0],
                'gender': 'Male'
            },
            {
                'username': 'carol_student',
                'email': 'carol@college.com',
                'password': 'student123',
                'first_name': 'Carol',
                'last_name': 'Davis',
                'address': '300 Hostel Road, Campus Area',
                'course': courses[1],  # MCA
                'session': sessions[0],
                'gender': 'Female'
            },
            {
                'username': 'david_student',
                'email': 'david@college.com',
                'password': 'student123',
                'first_name': 'David',
                'last_name': 'Lee',
                'address': '400 College Avenue, Campus Area',
                'course': courses[2],  # B.Tech
                'session': sessions[1],
                'gender': 'Male'
            },
            {
                'username': 'emma_student',
                'email': 'emma@college.com',
                'password': 'student123',
                'first_name': 'Emma',
                'last_name': 'Taylor',
                'address': '500 University Drive, Campus Area',
                'course': courses[3],  # MBA
                'session': sessions[1],
                'gender': 'Female'
            }
        ]

        for student_info in students_data:
            if not CustomUser.objects.filter(username=student_info['username']).exists():
                user = CustomUser.objects.create_user(
                    username=student_info['username'],
                    email=student_info['email'],
                    password=student_info['password'],
                    first_name=student_info['first_name'],
                    last_name=student_info['last_name'],
                    user_type='3'  # Student
                )
                student = Students.objects.create(
                    admin=user,
                    address=student_info['address'],
                    course_id=student_info['course'],
                    session_year_id=student_info['session'],
                    gender=student_info['gender']
                )
                self.stdout.write(self.style.SUCCESS(
                    f'  ✓ Created: {student_info["first_name"]} {student_info["last_name"]} '
                    f'({student_info["course"].course_name}) - {student_info["email"]}'
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f'  ⚠ Already exists: {student_info["first_name"]} {student_info["last_name"]}'
                ))

        # Summary
        self.stdout.write(self.style.SUCCESS('\n' + '='*60))
        self.stdout.write(self.style.SUCCESS('✓ SAMPLE DATA CREATION COMPLETED!'))
        self.stdout.write(self.style.SUCCESS('='*60))
        self.stdout.write(self.style.SUCCESS(f'\n📊 SUMMARY:'))
        self.stdout.write(self.style.SUCCESS(f'  • Courses: {Courses.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  • Session Years: {SessionYearModel.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  • Staff Members: {Staffs.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  • Subjects: {Subjects.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  • Students: {Students.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  • Total Users: {CustomUser.objects.count()}'))
        
        self.stdout.write(self.style.SUCCESS('\n📝 TEST CREDENTIALS:'))
        self.stdout.write(self.style.SUCCESS('  Admin: admin / admin123'))
        self.stdout.write(self.style.SUCCESS('  Staff: john.staff@college.com / staff123'))
        self.stdout.write(self.style.SUCCESS('  Student: alice@college.com / student123'))
        self.stdout.write(self.style.SUCCESS('\n' + '='*60 + '\n'))
