from django.shortcuts import render
from rest_framework.views import APIView
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response


#for order because it's the final list of order , it doen't have update option
class OrderView(APIView) :
    #create new order 
    def post(self,request) :
        try :
            serializer = OrderSerializer(data=request.META.get('Authorization'))
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data)
            else :
                return Response("Data isn't valid")
        except :
            return Response("Something went wrong")

    #find all orders according customer id
    def get(self , request) :
        try :
            customerId = request.META.get('Authorization')
            orders = Order.objects.filter(customer_id=customerId)
            serializer = OrderSerializer(orders , many=True)
            return Response(serializer.data)
        except :
            return Response("no order found")


class OrderViewByPk(APIView) :
    
    #find the order according order id
    def get(self ,request , pk) :
        try:
            order = Order.objects.filter(id=pk).first()
            serializer = OrderSerializer(order , many=False)
            return Response(serializer.data)
        except :
            return Response("Can't find the order")
    
    def delete(self , request,pk) :
        try :
            order = Order.objects.filter(id=pk).first()
            order.delete()
            return Response("Delete  order successfully")
        except :
            return Response("Can't find the order")