from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer

class CategoryView(APIView) :
    #create category
    def post(self,request) :
        try:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data)
            else :
                return Response("Can't create new category")
        except :
            return Response("Something went wrong")
    
    # get list of categories
    def get(self,request) :
        try :
            categories = Category.objects.all()
            serializer = CategorySerializer(categories , many=True)
            return Response(serializer.data)
        except :
            return Response("Something went wrong")



class CategoryViewByPk(APIView) :

    #get one category
    def get(self,request,pk):
        try :
            category = Category.objects.filter(id=pk).first()
            serializer = CategorySerializer(category , many=False)
            return Response(serializer.data)
        except :
            return Response("Can't find category")
    #update category
    def put(self,request,pk) :
        try : 
            category=Category.objects.filter(id=pk).first()
            serializer = CategorySerializer(instance=category , data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data)
            else :
                return Response("Can't find category")
        except :
            return Response("Something went wrong")
    
    #delete category
    def delete(self,request,pk) :
        try : 
            category = Category.objects.filter(id=pk).first()
            category.delete()
            return Response("Delete category successfully")
        except :
            return Response("Can't find category to delete")