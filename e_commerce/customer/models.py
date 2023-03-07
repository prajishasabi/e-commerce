from django.db import models
from common.models import Customer
from seller.models import Product
from datetime import date

# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        db_table = 'cart'

class Order(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    amount = models.FloatField()
    status = models.CharField(max_length=20,default='pending')
    provider_order_id = models.CharField( max_length=40,default='' )
    payment_id = models.CharField(max_length=36,default='')
    signature_id = models.CharField(max_length=128,default='' )

    class Meta:
        db_table = 'order_tb'


class Order_detail(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField()
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=20,default="pending") #update after payment confirmed
    payment_type = models.CharField(max_length=20,default='')
    order=models.ForeignKey(Order,on_delete=models.CASCADE,default=0)
 

    class Meta:
        db_table = 'order_details'


