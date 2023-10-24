from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from products_sell.models import ProductSell
from rest_framework.response import Response
from .serializers import ProductSerializer

# Create your views here.

class ProductView(APIView):
    #read a specific product according id
    def get(self , request) :
        try : 
            specific_product = Product.objects.filter(id =request.GET.get('id' , '')).first()
            return Response({
                'status_code' : 200 ,
                'message' : "product found",
                'data' : {'name' : specific_product.name , 'image':specific_product.image , "category" : specific_product.category , "subcategory" : specific_product.subcategory}
            })
        except : 
            return Response({
                'status_code' : 404 ,
                'message' : "product not found",
                'data' : {}
            })
    
    def post(self , request):
        try :
            # findProduct = ProductSell.objects.filter(name=request.data['name'] , user_id=request.headers).first()            
            findProduct = ProductSell.objects.filter(name=request.data['name'] ).first()
            if findProduct==None :   
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