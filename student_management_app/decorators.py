"""
Custom decorators for role-based access control
"""
from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps
from .models import CustomUser


def login_required_custom(view_func):
    """
    Decorator to check if user is authenticated
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Please login to access this page!")
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper


def admin_required(view_func):
    """
    Decorator to check if logged-in user is Admin/HOD
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Please login to access this page!")
            return redirect('login')
        
        if request.user.user_type != CustomUser.HOD:
            messages.error(request, "You don't have permission to access this page!")
            return redirect('home')
        
        return view_func(request, *args, **kwargs)
    return wrapper


def staff_required(view_func):
    """
    Decorator to check if logged-in user is Staff
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Please login to access this page!")
            return redirect('login')
        
        if request.user.user_type != CustomUser.STAFF:
            messages.error(request, "You don't have permission to access this page!")
            return redirect('home')
        
        return view_func(request, *args, **kwargs)
    return wrapper


def student_required(view_func):
    """
    Decorator to check if logged-in user is Student
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, "Please login to access this page!")
            return redirect('login')
        
        if request.user.user_type != CustomUser.STUDENT:
            messages.error(request, "You don't have permission to access this page!")
            return redirect('home')
        
        return view_func(request, *args, **kwargs)
    return wrapper


def ajax_required(view_func):
    """
    Decorator to check if request is AJAX
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            messages.error(request, "Invalid request!")
            return redirect('home')
        return view_func(request, *args, **kwargs)
    return wrapper
