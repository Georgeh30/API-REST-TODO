from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    confirm_email = models.EmailField(unique=True)
    nick_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    registration_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['confirm_email', 'username', 'nick_name', 'first_name', 'last_name']

    def __str__(self):
        return self.email
        