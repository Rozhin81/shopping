from django.db import models
from users.models import User
from products.models import Product


class Order(models.Model) :
    user_id = models.ForeignKey(User , null=False , blank=False)
    prod_id = models.ForeignKey(Product , null=False , blank=False)
    
