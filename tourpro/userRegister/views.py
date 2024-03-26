from django.contrib.auth import authenticate, login
import random
import string
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.core.mail import send_mail

def generate_username(F_name, L_name):
    username = (F_name.lower() + L_name.lower()).replace(' ', '')
    return username

def generate_password():
    # Generate a random password
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(10))
    return password


def user_register(request):
    if request.method == 'POST':
        # Retrieve form data
        F_name = request.POST.get('fname')
        L_name = request.POST.get('lname')
        Email = request.POST.get('email')
        Address = request.POST.get('address')
        Phone = request.POST.get('phone')
        
        # Generate username and password
        username = generate_username(F_name, L_name)
        password = generate_password()
        
        # Create user
        user = User.objects.create_user(username=username, email=Email, password=password, first_name=F_name, last_name=L_name)
        
        # Optionally, you can create a profile model and save additional information
        # For example:
        # user.profile.address = address
        # user.profile.phone = phone
        # user.profile.save()
        
        # Send email with credentials
        subject = 'Welcome to Our Website'
        message = f'Hello {F_name} {L_name},\n\nThank you for registering on our website.\n\nYour login credentials:\nUsername: {username}\nPassword: {password}\n\nBest regards,\nThe Management Team'
        send_mail(subject, message, 'your-email@example.com', [Email])
        
        # Log the user in
        login(request, user)
        
        # Redirect to dashboard or any other page after registration
        return redirect('user_login')  # Replace 'dashboard' with your dashboard URL name

    return render(request, 'regestration/user_register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing:gallary')  # Replace 'landing:gallary' with your gallery URL name
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'regestration/user_login.html', {'error_message': error_message})
    return render(request, 'regestration/user_login.html')




