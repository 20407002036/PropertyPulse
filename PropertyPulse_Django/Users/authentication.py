from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect


def user_login(request):
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
