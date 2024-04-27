from django.urls import path

# from PropertyPulse_Django.Users import views as userview
from . import views
from Users.views import register, login

urlpatterns = [
    path('', views.welcome, name='welcomePage'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
