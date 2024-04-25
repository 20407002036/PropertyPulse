from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use the concrete subclass of CustomUser
        fields = ('username', 'password1', 'password2')  # Specify the fields you want in the form
