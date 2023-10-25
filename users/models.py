from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager ,PermissionsMixin
# Create your models here.



class User(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'   #login with email
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email