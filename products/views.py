from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product , ProductChart
from products_sell.models import ProductSell
from rest_framework.response import Response
from .serializers import ProductSerializer , ChartSerializer
from django.utils.decorators import decorator_from_middleware
from customer.custom_middleware import CustomMiddleware
from django.utils.decorators import method_decorator

# middleware = decorator_from_middleware(CustomMiddleware)


class ProductView(APIView):

    @method_decorator(CustomMiddleware)
    #create new product
    def post(self , request):
        try :
            print(request.data)
            serializer = ProductSerializer(data = request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else :
                return Response( "data is not valid")
        except Exception as e:
            print(e)
            return Response("isn't valid")
    
    #get all created products 
    def get(self , request):
        products = Product.objects.all()
        serializer = ProductSerializer(products , many=True)
        return Response(serializer.data)
    



class ProductViewByPk(APIView) :

    #read a specific product according id
    def get(self , request , pk):  
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
            serializer = ProductSerializer(instance=product , data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data)
            else :
                return Response("Something Went wrong")
        except :
            print("error")
    
    #delete product
    def delete(self , request , pk):
        product = Product.objects.filter(id=pk).first()
        product.delete()
        return Response("Product successfully deleted!")




class ChartViewByPk(APIView) :
    def get(self , request , pk) :
        each_prod_chart = ProductChart.objects.filter(prod_id = pk)
        serializer = ChartSerializer(each_prod_chart , many=True)
        data = serializer.data
        return Response(data)

