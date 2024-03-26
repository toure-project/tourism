import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from .models import Managers


def home(request):
     return render(request, 'landing/index.html')


def hotel_dashboard(request):
    return render(request,  'hotel/hotel_dashboard.html' )

def transport_dashboard(request):
    return render(request,  'regestration/transport_dashboard.html' )

def reset_password(request):
    return render(request,  'regestration/reset_password.html' )

def generate_username(first_name, last_name):
    username = (first_name.lower() + last_name.lower()).replace(' ', '')
    return username

def generate_password():
    password_length = 10
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    return password


def register_manager(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        address = request.POST['address']
        phone_number = request.POST['phone']
        email = request.POST['email']
        role = request.POST['role']

        username = generate_username(first_name, last_name)
        password = generate_password()

        user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
        Managers.objects.create(user=user, first_name=first_name, last_name=last_name, address=address, phone_number=phone_number, email=email, role=role)
        
        # Send email with password
        subject = 'Welcome to Manager Project'
        message = f'Hello {first_name} {last_name},\n\nYour account has been created successfully.\nUsername: {username}\nPassword: {password}\n\nBest regards,\nThe Manager Project Team'
        send_mail(subject, message, 'your-email@example.com', [email])

        return redirect('login')
    return render(request, 'regestration/register.html')

# Remaining views remain the same




def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                role = user.managers.role
                if role == 'Hotel Manager':
                    return redirect('hotel_dashboard')
                elif role == 'Transport Manager':
                    return redirect('transport_dashboard')
                # Add more roles as needed
            except Managers.DoesNotExist:
                pass  # Handle case where user does not have a corresponding WorkerManager instance
        else:
            # Handle invalid login
            return redirect('register_manager')
    return render(request, 'regestration/login.html')


def NewUserLogin(request):
    return render(request,  'regestration/NewUserLogin.html' )


