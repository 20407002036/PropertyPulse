from django.shortcuts import render, redirect
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from .models.base_model import BaseModel
from .models.users import User

def login(requests):
    return render(requests, 'Users/login.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        second_name = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User(first_name, second_name, email, password)
        user.save()
        
        messages.success(request, 'Account created successfully!')
        return redirect('login')
    else:
        # form = UserCreationForm()
        return render(request, 'Users/register.html')
# removed context var on the render line, {'form': form}
