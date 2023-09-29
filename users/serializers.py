from rest_framework import serializers
from .models import User
from django.utils.encoding import smart_str,force_str , smart_bytes , DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode
import jwt , datetime
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Utils



class UserSerializer(serializers.ModelSerializer) :
    class Meta:
        model = User
        fields = ["name" , "email" , "phone", "password"]
        extra_kwargs={
            "password":{"write_only" : True}
        }

    def create(self , validate_data) :
        # print(validate_data)
        password = validate_data.pop("password" , None)
        instance = self.Meta.model(**validate_data)
        if password is not None :
            instance.set_password(password)
        instance.save()
        print(instance)
        return instance

    

# class ResetPasswordSerializer(serializers.Serializer) :
    # email = serializers.EmailField(min_length=2)
    # class Meta : 
    #     fields = ["email"]
    # def validate(self, attrs):
    #     try:
    #         email = attrs.get("email", '')
    #         if User.objects.filter(email=email).exists() :
    #             user = User.objects.get(email=email)
    #             payload = {
    #                 "id" : user.id ,
    #                 "email" :user.email ,
    #                 "exp" : datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
    #                 "iat" : datetime.datetime.utcnow()
    #             }
    #             token = jwt.encode(payload , "secret")       
    #             currrent_site = get_current_site(request=attrs["data"].get("request")).domain()
    #             relative_link = reverse('password-reset' , kwargs={'uidb64' : "uidb64" , 'token' : token})
    #             absurl = 'http://'+currrent_site+relative_link
    #             email_body = "Hi " + user.name + "use link below to reset your password "
    #             data = {"email_body" : email_body , "to_email" : user.email , "email_subject" : "Reset password"}
    #             Utils.send_email(data)
    #     except : 
    #         pass
    #     return super().validate(attrs)


class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only = True , min_length = 5)
    class Meta :
        fields = ["password"]
    def validate(self , data):
        password = data.get("password")
        token = self.context.get("kwargs").get("token")
        encoded_pk = self.context.get("kwargs").get("encoded_pk")
        if token is None or encoded_pk is None :
            raise serializers.ValidationError("Missing Data")
        user_email = urlsafe_base64_decode(encoded_pk).decode()
        user = User.objects.get(email=user_email)
        if not jwt.decode(token, "secret", algorithms=['HS256']) :
            raise serializers.ValidationError("token is invalid")
        user.set_password(password)
        user.save()
        return data



class EmailSerializer(serializers.Serializer) :
    email = serializers.EmailField()

    class Meta :
        fields = ["email"]

