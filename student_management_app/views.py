from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import logout, login
from .models import CustomUser, Staffs, Students, AdminHOD
from django.contrib import messages
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

@csrf_exempt
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def loginUser(request):
    return render(request, 'login_page.html')

@csrf_exempt
def doLogin(request):
    if request.method != 'POST':
        messages.error(request, "Invalid request method")
        return redirect('login')
    
    email_id = request.POST.get('email')
    password = request.POST.get('password')

    if not (email_id and password):
        messages.error(request, "Please provide all the details!!")
        return redirect('login')

    # Try to get user by email
    try:
        user = CustomUser.objects.get(email=email_id)
        # Authenticate with username and password
        user = authenticate(request, username=user.username, password=password)
    except CustomUser.DoesNotExist:
        user = None

    if user is None:
        messages.error(request, 'Invalid Login Credentials!!')
        return redirect('login')

    login(request, user)

    # Redirect based on user type
    if user.user_type == CustomUser.STUDENT:
        return redirect('student_home')
    elif user.user_type == CustomUser.STAFF:
        return redirect('staff_home')
    elif user.user_type == CustomUser.HOD:
        return redirect('admin_home')

    return redirect('home')

def registration(request):
    return render(request, 'registration.html')

@csrf_exempt
def doRegistration(request):
    if request.method != 'POST':
        messages.error(request, "Invalid request method")
        return redirect('registration')
        
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email_id = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirmPassword')
    user_type = request.POST.get('user_type')

    if not (first_name and last_name and email_id and password and confirm_password and user_type):
        messages.error(request, 'Please provide all the details!!')
        return redirect('registration')
    
    if password != confirm_password:
        messages.error(request, 'Both passwords should match!!')
        return redirect('registration')

    if CustomUser.objects.filter(email=email_id).exists():
        messages.error(request, 'User with this email already exists. Please login.')
        return redirect('registration')

    # Generate username from email
    username = email_id.split('@')[0]
    
    # Make username unique if it exists
    if CustomUser.objects.filter(username=username).exists():
        import random
        username = username + str(random.randint(100, 999))

    try:
        # Create user
        user = CustomUser()
        user.username = username
        user.email = email_id
        user.first_name = first_name
        user.last_name = last_name
        user.user_type = user_type
        user.set_password(password)
        user.save()

        # Create corresponding profile based on user type
        if user_type == CustomUser.STAFF:
            Staffs.objects.create(admin=user, address="")
        elif user_type == CustomUser.STUDENT:
            Students.objects.create(admin=user, address="", gender="Male")
        elif user_type == CustomUser.HOD:
            AdminHOD.objects.create(admin=user)

        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')
    except Exception as e:
        messages.error(request, f"Registration failed: {str(e)}")
        return redirect('registration')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

def get_user_type_from_email(email_id):
    try:
        email_user_type = email_id.split('@')[0].split('.')[1]
        return CustomUser.EMAIL_TO_USER_TYPE_MAP[email_user_type]
    except Exception as e:
        return None
