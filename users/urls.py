from django.contrib import admin
from django.urls import path 
from .views import RegisterView , LoginView , UserView , LogoutView ,ResetPassword ,PasswordReset ,EmailVerify


urlpatterns = [
    path("register/" , RegisterView.as_view()),
    path("login/" , LoginView.as_view()),
    path("user/" , UserView.as_view()),
    path("logout/" , LogoutView.as_view()),
    path("activate-user/<uidb64>/token/" , EmailVerify.active_user , name="activate"),
    path("password-reset/" ,PasswordReset.as_view()),
    path('password-reset/<str:encoded_pk>/<str:token>' , ResetPassword.as_view()  , name="reset-password"),
]