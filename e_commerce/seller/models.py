from django.db import models
from common.models import Seller

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 30 ,default='')
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)
    description = models.CharField(max_length = 200)
    stock = models.IntegerField()
    price = models.FloatField()
    pic = models.ImageField(upload_to = 'product/') 

    class Meta:
        db_table = 'product'
