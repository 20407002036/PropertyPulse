from django.shortcuts import render

# Create your views here.

def welcome(requests):
    return render(requests, 'Base/welcome.html')
