from django.core.management.base import BaseCommand
from student_management_app.models import Courses, SessionYearModel
from datetime import date


class Command(BaseCommand):
    help = 'Creates initial data (default course and session year)'

    def handle(self, *args, **kwargs):
        # Create default course if doesn't exist
        if not Courses.objects.exists():
            course = Courses.objects.create(course_name="Default Course")
            self.stdout.write(self.style.SUCCESS(f'Created default course: {course.course_name}'))
        else:
            self.stdout.write(self.style.WARNING('Courses already exist'))

        # Create default session year if doesn't exist
        if not SessionYearModel.objects.exists():
            session = SessionYearModel.objects.create(
                session_start_year=date(2024, 1, 1),
                session_end_year=date(2024, 12, 31)
            )
            self.stdout.write(self.style.SUCCESS(f'Created default session: 2024-2024'))
        else:
            self.stdout.write(self.style.WARNING('Session years already exist'))
        
        self.stdout.write(self.style.SUCCESS('Initial data created successfully!'))
