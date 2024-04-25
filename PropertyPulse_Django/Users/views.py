from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm


def login(requests):
    return render(requests, 'Users/login.html')
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'Users/register.html', {'form': form})
# removed context var on the render line, {'form': form}
