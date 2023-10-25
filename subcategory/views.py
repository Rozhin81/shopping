from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import SubCategory
from .serializers import SubCategorySerializer

class SubCategoryView(APIView) :
    #create SubCategory
    def post(self,request) :
        try:
            serializer = SubCategorySerializer(data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data)
            else :
                return Response("Can't create new SubCategory")
        except :
            return Response("Something went wrong")
    
    # get list of categories
    def get(self,request) :
        try :
            sub_category = SubCategory.objects.all()
            serializer = SubCategorySerializer(sub_category , many=True)
            return Response(serializer.data)
        except :
            return Response("Something went wrong")



class SubCategoryViewByPk(APIView) :

    #get one SubCategory
    def get(self,request,pk):
        try :
            sub_category = SubCategory.objects.filter(id=pk).first()
            serializer = SubCategorySerializer(sub_category , many=False)
            return Response(serializer.data)
        except :
            return Response("Can't find SubCategory")
    #update SubCategory
    def put(self,request,pk) :
        try : 
            sub_category=SubCategory.objects.filter(id=pk).first()
            serializer = SubCategorySerializer(instance=sub_category , data=request.data)
            if serializer.is_valid() :
                serializer.save()
                return Response(serializer.data)
            else :
                return Response("Can't find SubCategory")
        except :
            return Response("Something went wrong")
    
    #delete SubCategory
    def delete(self,request,pk) :
        try : 
            sub_category = SubCategory.objects.filter(id=pk).first()
            sub_category.delete()
            return Response("Delete SubCategory successfully")
        except :
            return Response("Can't find SubCategory to delete")