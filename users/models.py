from django.db import models
from django.contrib.auth.models import AbstractBaseUser , BaseUserManager ,PermissionsMixin
# Create your models here.



# class UserManager(BaseUserManager):
#     def create_user(self , email , password , **extra_fields) :
#         if not email :
#             raise ValueError("The email is not given")
#         email = self.normalize_email(email)
#         user = self.model(email=email , **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
    
#     def create_superuser(self , email , password , **extra_fields) :
#         extra_fields.setdefault('is_active' , True)
#         extra_fields.setdefault("is_stuff" , True)
#         extra_fields.setdefault("is_superuser" , True)

#         if not extra_fields.get('is_stuff') :
#             raise ValueError("SuperUser must be stuff")
        
#         if not extra_fields.get('is_superuser') :
#             raise ValueError("you sould be a superuser")
#         return self.create_user(email ,password , **extra_fields)
    



class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    username = None
    # is_active = models.BooleanField(default=True)
    # is_stuff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'   #login with email
    REQUIRED_FIELD = ['name' , 'phone' , 'email' , 'password']

    # objects = UserManager()

    def __str__(self):
        return self.email

    # def has_modeule_perms(self , app_label) :
    #     return True
    
    # def has_perm(self,perm , obj=None) :
    #     return True
