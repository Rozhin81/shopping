from django.db import models
from seller.models import Seller
from category.models import Category
from subcategory.models import SubCategory
from orders.models import Order

# grid_fs_storage = GridFSStorage(collection='myfiles' , base_url=''.join([settings.BASE_URL , 'myfiles/']) )

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