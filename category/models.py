from django.db import models

# Create your models here.

class Category(models.Model) :
    title = models.CharField(max_length=20)

    REQUIERED_FIELDS = ['title']

    def __str__(self) -> str:
        return self.title
    
    # class Meta :
    #     db_table = 'category'

    
