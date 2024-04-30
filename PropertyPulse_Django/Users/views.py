#!/usr/bin/python3

from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
# from .models.base_model import BaseModel
from .models import Users, Property

def login(requests):
    return render(requests, 'Users/login.html')


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
        return redirect('login')
    else:
        # form = UserCreationForm()
        return render(request, 'admin/registration/register.html')
# removed context var on the render line, {'form': form}
