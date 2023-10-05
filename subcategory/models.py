from djongo import models
from category.models import Category
# Create your models here.

class SubCategory(models.Model) :
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category , null=False , blank=False , on_delete=models.CASCADE)

    REQUIRED_FIELDS = ['title']
    
    def __str__(self) -> str:
        self.title

    class Meta :
        db_table = "subcategory"
