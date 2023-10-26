from django.db import models
from products.models import Product


class Order(models.Model) :
    prod_id = models.ForeignKey(Product , null=False , blank=False)
    date = models.DateTimeField()
    
