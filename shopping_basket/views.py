from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Basket
from .serializers import BasketSerializer
import jwt

#bayad baraye hamashon token emal beshe (ke tooye hamoon middleware  in amaliyat anjam mishe : request.data['userId'] = token.id )
class BasketView(APIView) :

    #create shopping basket
    def post(self , request) :
        try :
            #--------use decorator for jwt----------------
            token= jwt.verify(request.META.get('Authorization'))
            #---------------------------------------------
            request.data['cust_id'] = token.id
            serializer = BasketSerializer(data= request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data)
            else :
                return Response("Data ins't valid")
        except :
            return Response("Something went wrong")
        
    def get(self,request) :
        #find all orders according customer_id
        # orders=Basket.objects.filter(id=token.id)
        # serializer = BasketSerializer(orders , many = True)
        # return Response(orders)
        pass


class BasketViewByPk(APIView) :

    #get the specific basket
    def get(self,request ,pk) :
        orderItem = Basket.objects.filter(id=pk).first()
        serializer = BasketSerializer(orderItem)
        return Response(serializer.data)

    #update the basket
    def put(self , request , pk) :
        orderItem = Basket.objects.filter(id=pk).first()
        # request.data['cust_id'] = token.id
        serializers = BasketSerializer(instance=orderItem , data=request.data)
        if serializers.is_valid() :
            serializers.save()
            return Response(serializers.data)
        else :
            return Response("Can't update your basket")

    def delete(self,request , pk) :
        orderItem = Basket.objects.filter(id=pk).first()
        orderItem.delete()
        return Response("Delete Successfully")

