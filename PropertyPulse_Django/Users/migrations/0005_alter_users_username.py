# Generated by Django 4.2.4 on 2024-04-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_users_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(default='NewUser', max_length=128, unique=True),
        ),
    ]
