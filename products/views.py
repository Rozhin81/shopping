from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from rest_framework.response import Response


# Create your views here.

class ProductView(APIView):
    #read a specific product according id
    def get(self , request) :
        # try : 
            # print(request.GET.get('id' , ''))
        specific_product = Product.objects.filter(id =request.GET.get('id' , '')).first()
        print(specific_product.name)
        return Response({
            'status_code' : 200 ,
            'message' : "product found",
            'data' : "{specific_product}"
        })
        # except : 
        #     return Response({
        #         'status_code' : 404 ,
        #         'message' : "product not found",
        #         'data' : {}
        #     })
    
    def post(self , request):
        try :
            print(request.data)
            Product.objects.create(request.data)
            return Response({
                'status_code' : 200 ,
                "message" : "successfully created",
                'data' : {}
            })
        except :
            return Response({
                'status_code' : 200 ,
                "message" : "successfully created",
                'data' : {}
            })