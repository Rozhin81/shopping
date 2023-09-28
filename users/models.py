from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager ,PermissionsMixin
# Create your models here.



class UserManager(BaseUserManager):
    def create_user(self , email , password , is_admin = False ,is_stuff=False , **extra_fields) :
        if not email :
            raise ValueError("The email is not given")
        if not password :
            raise ValueError("User must have password")
        user = self.model(email=self.normalize_email(email) , **extra_fields)
        user.is_admin = is_admin
        user.is_staff = is_stuff
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self , email , password , is_admin = True ,is_stuff=True ,is_active=True , **extra_fields) :
        return self.create_user(email ,password , **extra_fields)
    



class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    email_verified=models.BooleanField(default=False)
    username = None
    is_active = models.BooleanField(default=True)
    is_stuff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'   #login with email
    REQUIRED_FIELDS = ['phone' , 'password' ]

    objects = UserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        db_table="users"

    # def has_modeule_perms(self , app_label) :
    #     return True
    
    # def has_perm(self,perm , obj=None) :
    #     return True
