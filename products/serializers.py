from rest_framework import serializers
from .models import Product , ProductChart


class ProductSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Product
        fields = '__all__'


class ChartSerializer(serializers.ModelSerializer) :
    class Meta :
        model = ProductChart
        fields = '__all__'
