from django.shortcuts import render
from rest_framework.views import APIView 
from .serializers import UserSerializer , ResetPasswordSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt , datetime
from rest_framework import generics , status , viewsets
from . import serializers
from base64 import urlsafe_b64encode
from django.utils.encoding import force_bytes
from django.urls import reverse


#Register Part
class RegisterView(APIView):
    def post(self , request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
#Login Part
class LoginView(APIView):
    def post(self,request) :
        email = request.data['email']
        password = request.data["password"]

        user=User.objects.filter(email=email).first()
        if user is None :
            raise AuthenticationFailed("User not found")

        if not user.check_password(password) :
            raise AuthenticationFailed("Incorrect password")
        
        payload = {
            "id" : user.id ,
            "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
            "iat" : datetime.datetime.utcnow()
        }
        token = jwt.encode(payload , "secret")
        
        response = Response()
        response.set_cookie(key="jwt" , value=token , httponly=True)
        response.data ={
            "status" : 200 ,
            "message" : "successfully login",
            "jwt" : token
        }

        return response


class UserView(APIView) :
    def get(self , request) :
        token = request.COOKIES.get("jwt")

        if not token :
            raise AuthenticationFailed("Unauthenticated")
        try:
            payload = jwt.decode(token , "secret" , algorithms=["HS256"])
        except jwt.ExpiredSignatureError: 
            raise AuthenticationFailed("Unauthenticated")
        
        user = User.objects.filter(id=payload["id"]).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self , request) :
        response = Response()
        response.delete_cookie("jwt")
        response.data = {
            "message" : "success"
        }
        return response
    
class RequestPasswordResetEmail(generics.GenericAPIView) :
    serializer_class = ResetPasswordSerializer
    def post(self , request) :
        data = { "request" : request , "data":request.data}
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

class PasswordReset(generics.GenericAPIView) :
    serializer_class = serializers.EmailSerializer
    def post(self , request) :
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        user = User.objects.filter(email=email).first()
        if user :
            encoded_pk = urlsafe_b64encode(force_bytes(user.email))
            payload ={
                'id' : user.id,
                'email' : user.email,
                "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
                "iat" : datetime.datetime.utcnow()
            }
            token = jwt.encode(payload , "secret")
            reset_url = reverse( "reset-password" , kwargs={"encoded_pk" : encoded_pk , "token" : token})
            reset_url = f"localhost:8000{reset_url}"
            
            return Response({
                "message" : f"Your password reset link : {reset_url}",
                "status" : status.HTTP_200_OK
            })
        else :
            return Response({
                "message" : "User doesn't exist",
                "status" : status.HTTP_400_BAD_REQUEST
            })


class ResetPassword(generics.GenericAPIView):
    serializer_class=ResetPasswordSerializer
    def patch(self , request , *args , **kwargs) :
        serializer = self.serializer_class(data = request.data , context={"kwargs":kwargs})
        serializer.is_valid(raise_exception=True)
        return Response({
            "message" : "Password reset complete",
            "status" : status.HTTP_200_OK
        })