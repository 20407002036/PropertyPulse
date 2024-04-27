from django.db import models

class Users(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128, blank=True, null=True)
    user_type = models.CharField(max_length=128, choices=[('Tenant', 'Tenant'), ('Owner', 'Owner')])

    def __str__(self):
        return self.email

class Property(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=128)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)  # Assuming each property belongs to one user
    description = models.TextField()

    def __str__(self):
        return self.name
