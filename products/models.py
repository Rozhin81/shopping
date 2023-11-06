from django.db import models
from seller.models import Seller
from category.models import Category
from subcategory.models import SubCategory
from orders.models import Order
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_save
# from django.utils import timezone


class Product(models.Model) :
    category = models.ForeignKey(Category , null=True , blank=True , on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory , null=True , blank=True , on_delete=models.CASCADE)
    seller_id = models.ManyToManyField(Seller, null=True , blank=True)
    orderId = models.ManyToManyField(Order, null=True , blank=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    maker = models.CharField(max_length=50)
    built_in = models.CharField(max_length=30)
    description = models.TextField()
    # image = models.ImageField(upload_to='products' , storage=grid_fs_storage) 
    stars = models.IntegerField()
    
    REQUIRED_FIELDS = ['maker' , 'name','built_in' ,'image']

    def __str__(self) -> str:
        return self.name
    

@receiver(post_save , sender=Product)
def create_chart(sender , instance , created , **kwargs) :
        obj = ProductChart(price=instance.price,date=datetime.now(),prod_id=instance)
        obj.save()

# @receiver(post_save , sender=Product)
# def save_chart(sender , instance , **kwargs) :
#     instance.ProductChart.save()

class ProductChart(models.Model) :
    prod_id=models.ForeignKey(Product ,  on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    date =  models.DateField()
    def __str__(self):
        return self.prod_id
    

