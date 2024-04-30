#!/usr/bin/python3

# from django.contrib.auth.forms import UserCreationForm
# from .models.base_model import BaseModel
from .models import Users, Property
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user is not None:
            # User authentication successful
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('home')  # Redirect to home page or any other desired page after login
        else:
            # User authentication failed
            messages.error(request, 'Invalid username or password. Please try again.')

    # If GET request or authentication failed, render the login page
    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        second_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Users(first_name=first_name, last_name=second_name, email=email, password=password)
        print(user)
        user.save()

        messages.success(request, 'Account created successfully!')
        return redirect('user_login')
    else:
        # form = UserCreationForm()
        return render(request, 'admin/registration/register.html')
# removed context var on the render line, {'form': form}
