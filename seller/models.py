from djongo import models

# Create your models here.
class Seller(models.Model) :
    name = models.CharField(max_length=50)
    phone = models.IntegerField(unique=True)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True)
    activation = models.BooleanField(default=False)
    identifier_code =  models.CharField(max_length=10 , unique=True)

    REQUIRED_FIELDS = ['phone' , 'password' , 'email' , 'identifier_code']

    def __str__(self) -> str:
        self.email
    
    class Meta :
        db_table = "seller"