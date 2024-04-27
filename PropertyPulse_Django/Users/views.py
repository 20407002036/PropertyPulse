from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .models import *

def login(requests):
    return render(requests, 'Users/login.html')


def register(request):
    if request.method == 'POST':
        firstName = request.form['first_name']
        secondName = request.form['second_name']
        email = request.form['email']
        password = request.form['password']
        
        user = User(firstName,secondName,email,password)
        user.save()
        
        messages.success(request, 'Account created successfully!')
        return redirect('login')
    else:
        # form = UserCreationForm()
        return render(request, 'Users/register.html')
# removed context var on the render line, {'form': form}
