from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Define any additional fields you need

    class Meta:
        # Add or change the related_name for groups and user_permissions
        # This resolves the clashes with the default User model
        # For example, you can use 'customuser_groups' and 'customuser_user_permissions'
        # Adjust as needed based on your project's naming conventions
        # Ensure that the related_name is unique and does not clash with other models
        # Also, consider using 'related_query_name' if needed
        # See Django documentation for more information: https://docs.djangoproject.com/en/4.0/ref/models/options/#related-name
        # Example:
        # related_name='customuser_groups', related_query_name='customuser_group'
        permissions = (("can_vote", "Can vote"),)
        abstract = True
