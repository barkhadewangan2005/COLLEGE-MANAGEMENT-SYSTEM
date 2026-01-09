from django.core.management.base import BaseCommand
from student_management_app.models import (
    CustomUser, Courses, SessionYearModel, Staffs, Students, Subjects,
    Announcement, Notification, FeedBackStudent, FeedBackStaffs,
    LeaveReportStudent, LeaveReportStaff
)
from datetime import date, datetime, timedelta

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

        # Get admin user
        admin_user = CustomUser.objects.filter(user_type='1').first()
        if not admin_user:
            admin_user = CustomUser.objects.create_user(
                username='admin',
                email='admin@college.com',
                password='admin123',
                first_name='Admin',
                last_name='User',
                user_type='1'
            )
            self.stdout.write(self.style.SUCCESS('  ✓ Created: Admin User'))

        # Create Announcements
        self.stdout.write(self.style.WARNING('\n📢 Creating Announcements...'))
        announcements_data = [
            {
                'title': 'Welcome to New Academic Year 2024',
                'message': 'Dear students and faculty, we are excited to welcome you to the new academic year. Please check your course schedules and ensure all documents are updated.',
                'target_audience': 'all',
                'urgency': 'medium',
                'category': 'general',
                'expiry_date': datetime.now() + timedelta(days=30)
            },
            {
                'title': 'Mid-Semester Examination Schedule',
                'message': 'Mid-semester examinations will begin from next week. Please check the examination portal for detailed schedules and seating arrangements.',
                'target_audience': 'students',
                'urgency': 'high',
                'category': 'academic',
                'expiry_date': datetime.now() + timedelta(days=14)
            },
            {
                'title': 'Faculty Development Workshop',
                'message': 'A workshop on modern teaching methodologies will be conducted for all faculty members. Participation is mandatory.',
                'target_audience': 'staff',
                'urgency': 'medium',
                'category': 'administrative',
                'expiry_date': datetime.now() + timedelta(days=7)
            },
            {
                'title': 'Annual Sports Meet Registration',
                'message': 'Registration for the annual sports meet is now open. Students interested in participating should register through the student portal.',
                'target_audience': 'students',
                'urgency': 'low',
                'category': 'events',
                'expiry_date': datetime.now() + timedelta(days=21)
            }
        ]

        for announcement_data in announcements_data:
            announcement, created = Announcement.objects.get_or_create(
                title=announcement_data['title'],
                defaults={
                    'message': announcement_data['message'],
                    'target_audience': announcement_data['target_audience'],
                    'urgency': announcement_data['urgency'],
                    'category': announcement_data['category'],
                    'expiry_date': announcement_data['expiry_date'],
                    'created_by': admin_user
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'  ✓ Created: {announcement.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'  ⚠ Already exists: {announcement.title}'))

        # Create Notifications
        self.stdout.write(self.style.WARNING('\n🔔 Creating Notifications...'))
        all_users = list(CustomUser.objects.all())
        notification_data = [
            {
                'title': 'Profile Update Required',
                'message': 'Please update your profile information including contact details and emergency contacts.',
                'notification_type': 'general',
                'urgency': 'medium',
                'category': 'administrative'
            },
            {
                'title': 'Attendance Alert',
                'message': 'Your attendance in Data Structures is below 75%. Please improve your attendance.',
                'notification_type': 'attendance',
                'urgency': 'high',
                'category': 'academic'
            },
            {
                'title': 'Leave Request Approved',
                'message': 'Your leave request for medical reasons has been approved.',
                'notification_type': 'leave',
                'urgency': 'low',
                'category': 'administrative'
            },
            {
                'title': 'Result Published',
                'message': 'Your semester examination results have been published. Check your student portal.',
                'notification_type': 'result',
                'urgency': 'medium',
                'category': 'academic'
            },
            {
                'title': 'Feedback Response',
                'message': 'Your feedback has been reviewed. Thank you for your valuable input.',
                'notification_type': 'feedback',
                'urgency': 'low',
                'category': 'general'
            }
        ]

        for user in all_users:
            for notif_data in notification_data:
                notification, created = Notification.objects.get_or_create(
                    user=user,
                    title=notif_data['title'],
                    defaults={
                        'message': notif_data['message'],
                        'notification_type': notif_data['notification_type'],
                        'urgency': notif_data['urgency'],
                        'category': notif_data['category']
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'  ✓ Created notification for {user.username}: {notif_data["title"]}'))

        # Create Student Feedback
        self.stdout.write(self.style.WARNING('\n💬 Creating Student Feedback...'))
        students = Students.objects.all()
        feedback_data = [
            'The teaching quality is excellent and the course content is very relevant.',
            'More practical sessions would be helpful for better understanding.',
            'The library resources are adequate but could be improved.',
            'Faculty members are very supportive and approachable.',
            'The campus facilities need better maintenance.'
        ]

        for student in students:
            for i, feedback_text in enumerate(feedback_data):
                feedback, created = FeedBackStudent.objects.get_or_create(
                    student_id=student,
                    feedback=feedback_text,
                    defaults={
                        'feedback_reply': 'Thank you for your feedback. We will consider your suggestions for improvement.' if i % 2 == 0 else ''
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'  ✓ Created feedback for {student.admin.username}'))

        # Create Staff Feedback
        self.stdout.write(self.style.WARNING('\n👨‍🏫 Creating Staff Feedback...'))
        staffs = Staffs.objects.all()
        staff_feedback_data = [
            'The administrative support is good but could be more efficient.',
            'More professional development opportunities would be beneficial.',
            'The work environment is conducive to teaching and research.',
            'Salary and benefits are competitive in the industry.',
            'More research funding would help in academic pursuits.'
        ]

        for staff in staffs:
            for i, feedback_text in enumerate(staff_feedback_data):
                feedback, created = FeedBackStaffs.objects.get_or_create(
                    staff_id=staff,
                    feedback=feedback_text,
                    defaults={
                        'feedback_reply': 'Thank you for your feedback. We value your input for continuous improvement.' if i % 2 == 0 else ''
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'  ✓ Created feedback for {staff.admin.username}'))

        # Create Student Leave Requests
        self.stdout.write(self.style.WARNING('\n📝 Creating Student Leave Requests...'))
        leave_reasons = [
            'Medical emergency - fever and flu',
            'Family function - cousin marriage',
            'Personal reasons - urgent work at home',
            'Sports event participation',
            'Medical checkup appointment'
        ]

        for student in students:
            for i, reason in enumerate(leave_reasons):
                leave_date = (datetime.now() + timedelta(days=i+1)).strftime('%Y-%m-%d')
                leave, created = LeaveReportStudent.objects.get_or_create(
                    student_id=student,
                    leave_date=leave_date,
                    defaults={
                        'leave_message': reason,
                        'leave_status': 1 if i % 2 == 0 else 0  # Alternate approved/pending
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'  ✓ Created leave request for {student.admin.username}: {reason}'))

        # Create Staff Leave Requests
        self.stdout.write(self.style.WARNING('\n🏖️ Creating Staff Leave Requests...'))
        staff_leave_reasons = [
            'Medical leave - doctor appointment',
            'Personal leave - family matters',
            'Casual leave - personal work',
            'Earned leave - vacation',
            'Sick leave - health issues'
        ]

        for staff in staffs:
            for i, reason in enumerate(staff_leave_reasons):
                leave_date = (datetime.now() + timedelta(days=i+2)).strftime('%Y-%m-%d')
                leave, created = LeaveReportStaff.objects.get_or_create(
                    staff_id=staff,
                    leave_date=leave_date,
                    defaults={
                        'leave_message': reason,
                        'leave_status': 1 if i % 2 == 0 else 0  # Alternate approved/pending
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'  ✓ Created leave request for {staff.admin.username}: {reason}'))

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
        self.stdout.write(self.style.SUCCESS(f'  • Announcements: {Announcement.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  • Notifications: {Notification.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  • Student Feedback: {FeedBackStudent.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  • Staff Feedback: {FeedBackStaffs.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  • Student Leave Requests: {LeaveReportStudent.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  • Staff Leave Requests: {LeaveReportStaff.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'  • Total Users: {CustomUser.objects.count()}'))
        
        self.stdout.write(self.style.SUCCESS('\n📝 TEST CREDENTIALS:'))
        self.stdout.write(self.style.SUCCESS('  Admin: admin / admin123'))
        self.stdout.write(self.style.SUCCESS('  Staff: john.staff@college.com / staff123'))
        self.stdout.write(self.style.SUCCESS('  Student: alice@college.com / student123'))
        self.stdout.write(self.style.SUCCESS('\n' + '='*60 + '\n'))
