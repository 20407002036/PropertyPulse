from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add custom fields if needed
    # For example:
    # phone_number = models.CharField(max_length=15)
    pass
