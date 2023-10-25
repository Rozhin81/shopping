from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from products_sell.models import ProductSell
from rest_framework.response import Response
from .serializers import ProductSerializer

# Create your views here.

class ProductView(APIView):
    #create new product
    def post(self , request):
        # try :
            serializer = ProductSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else :
                return Response( "data is not valid")
        # except :
        #     return Response("isn't valid")
    
    #get all created products 
    def get(self , request):
        products = Product.objects.all()
        serializer = ProductSerializer(products , many=True)
        return Response(serializer.data)
    



class ProductViewByPk(APIView) :

    #read a specific product according id
    def get(self , request , pk):   #not work for pk argument
        try : 
            specific_product = Product.objects.filter(id=pk).first()
            serializer= ProductSerializer(specific_product , many=False)
            return Response(serializer.data)
        except : 
            return Response("product not found")
        
    #update products information
    def put(self , request , pk): 
        try :
            product = Product.objects.filter(id=pk).first()
            print(product)
            serializer = ProductSerializer(instance=product , data=request.data)
            if serializer.is_valid() :
                serializer.save()
            return Response(serializer.data)
            # else :
            #     return Response("Something Went wrong")
        except :
            print("error")
    
    #delete product
    def delete(self , request , pk):
        product = Product.objects.filter(id=pk).first()
        product.delete()
        return Response("Product successfully deleted!")
