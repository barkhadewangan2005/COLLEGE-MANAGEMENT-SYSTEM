"""
Custom middleware for request processing
"""
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages


class RoleBasedAccessMiddleware:
    """
    Middleware to restrict access based on user roles
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # URLs that don't require authentication
        public_urls = [
            reverse('home'),
            reverse('contact'),
            reverse('login'),
            reverse('doLogin'),
            reverse('registration'),
            reverse('doRegistration'),
            reverse('logout_user'),
            '/admin/',
            '/static/',
            '/media/',
            '/__debug__/',
        ]
        
        # Check if current path is public
        current_path = request.path
        is_public = any(current_path.startswith(url) for url in public_urls)
        
        if is_public:
            response = self.get_response(request)
            return response
            
        # Check authentication for protected routes
        if not request.user.is_authenticated:
            if not current_path.startswith('/admin/'):
                messages.warning(request, "Please login to access this page!")
                return redirect('login')
        else:
            # Role-based routing
            user_type = request.user.user_type
            
            # Admin routes
            if current_path.startswith('/admin_') or current_path.startswith('/add_') or \
               current_path.startswith('/manage_') or current_path.startswith('/edit_') or \
               current_path.startswith('/delete_') or current_path.startswith('/check_'):
                if user_type != 1:  # CustomUser.HOD
                    messages.error(request, "You don't have permission to access this page!")
                    return redirect('home')
            
            # Staff routes
            elif current_path.startswith('/staff_') or current_path.startswith('/get_students') or \
                 current_path.startswith('/save_attendance') or current_path.startswith('/get_attendance') or \
                 current_path.startswith('/update_attendance'):
                if user_type != 2:  # CustomUser.STAFF
                    messages.error(request, "You don't have permission to access this page!")
                    return redirect('home')
            
            # Student routes
            elif current_path.startswith('/student_'):
                if user_type != 3:  # CustomUser.STUDENT
                    messages.error(request, "You don't have permission to access this page!")
                    return redirect('home')
        
        response = self.get_response(request)
        return response


class LoginRedirectMiddleware:
    """
    Middleware to redirect authenticated users from login page to their dashboard
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        # Check if user is trying to access login page while authenticated
        if request.path == reverse('login') and request.user.is_authenticated:
            user_type = request.user.user_type
            
            if user_type == 1:  # Admin
                return redirect('admin_home')
            elif user_type == 2:  # Staff
                return redirect('staff_home')
            elif user_type == 3:  # Student
                return redirect('student_home')
        
        response = self.get_response(request)
        return response
