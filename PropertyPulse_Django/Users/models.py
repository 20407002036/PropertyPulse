import uuid
from django.db import models

class Users(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128, blank=True, null=True)
    USER_TYPES = [
        ('Tenant', 'Tenant'),
        ('Owner', 'Owner'),
    ]
    user_type = models.CharField(max_length=128, choices=USER_TYPES)

    def __str__(self):
        return self.email


class Property(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=128)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
