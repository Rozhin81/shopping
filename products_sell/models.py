from djongo import models
from seller.models import Seller
from products.models import Product


class ProductSell(models.Model) :
    seller_id = models.ForeignKey(Seller , null=False , blank=False , on_delete=models.CASCADE )
    product_id = models.ForeignKey(Product , null=False , blank=False , on_delete=models.CASCADE)
    price = models.IntegerField()
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=20)
    count = models.IntegerField()

    REQUIRED_FIELDS = ['name' , 'color' , 'price' , 'count']

    def __str__(self) -> str:
        self.name

    class Meta :
        db_table = 'products_sell'