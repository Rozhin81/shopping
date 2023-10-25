from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Product
        # fields = ['category' , 'subcategory' ,'name' , 'seller_id','maker','built_in','description','stars']
        fields = '__all__'