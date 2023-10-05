from djongo import models
from users.models import User
from category.models import Category
from django.conf import settings
from djongo.storage import GridFSStorage


grid_fs_storage = GridFSStorage(collection='myfiles' , base_url=''.join([settings.BASE_URL , 'myfiles/']) )

class Product(models.Model) :
    category = models.ForeignKey(Category , null=False , blank=False , on_delete=models.CASCADE)           
    # number = 
    #price = 
    name = models.CharField(max_length=50)
    user_id = models.ManyToManyField(User)
    maker = models.CharField(max_length=50)
    built_in = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='products' , storage=grid_fs_storage) 
    
    REQUIRED_FIELDS = ['maker' , 'name','built_in' ,'image']

    class Meta :
        db_table = "products"