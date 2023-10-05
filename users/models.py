from djongo import models
from djongo.models import UniqueConstraint
from django.contrib.auth.models import AbstractUser , BaseUserManager ,PermissionsMixin
# Create your models here.



class User(AbstractUser):
    username = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    email_verified=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_stuff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'   #login with email
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    class Meta:
        db_table="users"
        constraints = [
            UniqueConstraint(fields = ['email' , 'phone'] , name = "unique")
        ]