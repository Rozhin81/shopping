from django.db import models
from customer.models import Customer

from datetime import datetime


class Order(models.Model) :
    customer_id = models.ForeignKey(Customer , null=False , blank=False , on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now , blank=True)
