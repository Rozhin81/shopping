from django.db import models
from products.models import Product
from orders.models import Order
from customer.models import Customer


class Basket(models.Model) :
    product_id = models.ForeignKey(Product , null=False , blank=False ,on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order , null=False , blank=False , on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer , null=True , blank=True ,on_delete=models.CASCADE)
    color = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    number = models.IntegerField()