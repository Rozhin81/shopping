from django.contrib.sites.shortcuts import get_current_site
from rest_framework.views import APIView 
from .serializers import CustomerSerializer , ResetPasswordSerializer
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.exceptions import AuthenticationFailed
from .models import Customer
import jwt , datetime
from rest_framework import generics , status , viewsets
from . import serializers
from base64 import urlsafe_b64encode
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes , force_str  , DjangoUnicodeDecodeError
from django.urls import reverse
from django.template.loader import render_to_string
from .utils import Utils
# from rest_framework.permissions import IsAuthenticated


class EmailVerify:
    def send_action_email(customer , request):
        payload ={
            'id' : customer.id,
            'email' : customer.email,
            "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=15),
            "iat" : datetime.datetime.utcnow()
        }
        current_site = get_current_site(request)
        email_subject = "Activate your account"
        email_body = render_to_string("users/activate.html" , {
            "user" : customer,
            "domain" : current_site,
            'uid': urlsafe_b64encode(force_bytes(customer.id)),
            'token' : jwt.encode(payload , 'secret')
        })
        Utils.send_email({"email_subject" : email_subject , "email_body" :email_body , "to_email" : customer.email})
    
    def active_user(request , uidb64 , token) :
        try :
            uid = force_str(urlsafe_base64_decode(uidb64))
            customer= Customer.objects.get(id=uid)
        except Exception as e :
            customer=None
        if customer and jwt.decode(token) :
            customer.email_verified= True
            customer.save()
            EmailVerify.send_action_email(customer , request)
            return Response({
                "message" : "Verified your email",
                "status" : status.HTTP_200_OK
            })

#Register Part
class RegisterView(APIView):

    def post(self , request):
        try :
            serializer = CustomerSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except:
            return Response({
                'status_code' : 409 ,
                'message' : "there is an account with this email",
                'data' : {}
            })



#Login Part
class LoginView(APIView):
    def post(self,request) :

        email = request.data['email']
        password = request.data["password"]

        customer = Customer.objects.filter(email=email).first()
        if customer is None :
            raise AuthenticationFailed("User not found")

        if not customer.check_password(password) :
            raise AuthenticationFailed("Incorrect password")
        
        if not customer.email_verified :
            raise AuthenticationFailed("Please , first verify your Email")

        payload = {
            "id" : customer.id 
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


class CustomerView(APIView) :
    def get(self , request) :
        token = request.COOKIES.get("jwt")

        if not token :
            raise AuthenticationFailed("Unauthenticated")
        try:
            payload = jwt.decode(token , "secret" , algorithms=["HS256"])
        except jwt.ExpiredSignatureError: 
            raise AuthenticationFailed("Unauthenticated")
        
        customer = Customer.objects.filter(id=payload["id"]).first()
        serializer = CustomerSerializer(customer)

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
        customer = Customer.objects.filter(email=email).first()
        if customer :
            encoded_pk = urlsafe_b64encode(force_bytes(customer.id))
            payload ={
                'id' : customer.id,
                'email' : customer.email,
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