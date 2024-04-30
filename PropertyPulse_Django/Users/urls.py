from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='user_login'),
    path('register', views.register, name='register'),

]
