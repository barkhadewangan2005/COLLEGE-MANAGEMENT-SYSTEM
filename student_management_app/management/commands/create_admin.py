from django.core.management.base import BaseCommand
from student_management_app.models import CustomUser, AdminHOD

class Command(BaseCommand):
    help = 'Creates an admin/HOD user for the College Management System'

    def handle(self, *args, **kwargs):
        # Check if admin already exists
        if CustomUser.objects.filter(username='admin').exists():
            self.stdout.write(self.style.WARNING('Admin user already exists!'))
            admin_user = CustomUser.objects.get(username='admin')
        else:
            # Create admin user
            admin_user = CustomUser.objects.create_user(
                username='admin',
                email='admin@college.com',
                password='admin123',
                first_name='Admin',
                last_name='User',
                user_type='1'  # HOD
            )
            self.stdout.write(self.style.SUCCESS(f'✓ Created admin user: {admin_user.username}'))

        # Check if AdminHOD profile exists
        if not hasattr(admin_user, 'adminhod'):
            AdminHOD.objects.create(admin=admin_user)
            self.stdout.write(self.style.SUCCESS('✓ Created AdminHOD profile'))
        else:
            self.stdout.write(self.style.WARNING('AdminHOD profile already exists'))

        self.stdout.write(self.style.SUCCESS('\n=== Admin User Created Successfully ==='))
        self.stdout.write(self.style.SUCCESS(f'Username: admin'))
        self.stdout.write(self.style.SUCCESS(f'Email: admin@college.com'))
        self.stdout.write(self.style.SUCCESS(f'Password: admin123'))
        self.stdout.write(self.style.SUCCESS(f'User Type: HOD (Admin)'))
        self.stdout.write(self.style.SUCCESS(f'\nLogin at: http://127.0.0.1:8000/login'))
