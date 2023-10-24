from django.db import models
from seller.models import Seller
from django.conf import settings
from category.models import Category
from subcategory.models import SubCategory


# grid_fs_storage = GridFSStorage(collection='myfiles' , base_url=''.join([settings.BASE_URL , 'myfiles/']) )

class Product(models.Model) :
    category = models.ForeignKey(Category , null=False , blank=False , on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory , null=False , blank=False , on_delete=models.CASCADE)           
    name = models.CharField(max_length=50)
    seller_id = models.ManyToManyField(Seller)
    maker = models.CharField(max_length=50)
    built_in = models.CharField(max_length=30)
    description = models.TextField()
    # image = models.ImageField(upload_to='products' , storage=grid_fs_storage) 
    stars = models.IntegerField()
    
    REQUIRED_FIELDS = ['maker' , 'name','built_in' ,'image']

    def __str__(self) -> str:
        return self.name

    # class Meta :
    #     db_table = "products"