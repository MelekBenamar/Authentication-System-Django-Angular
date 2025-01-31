from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)

    email = models.CharField(max_length=255, unique=True)

    password = models.CharField(max_length=255)

    # in django, by default the username is required 
    # Overide the username
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []






# -- models --
# Create models for your custom data tables in the database.
# This is the core of Django's Object-Relational Mapping (ORM).
# You use it to define fields and relationships between different entities in your database

# -- AbstractUser --
# Django’s built-in User model
# Already includes important fields like:
    # username
    # email
    # password
    # is_staff
    # is_active

# You can add additional fields to this user model, such as (date_of_birth, profile_picture, or phone_number,... )
