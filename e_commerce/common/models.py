from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    address = models.CharField(max_length = 200)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length = 15)
    password = models.CharField(max_length = 20,default ='')
    status = models.CharField(max_length = 20, default = 'active')

    class Meta:
        db_table = 'customer'

class Seller(models.Model):
    seller_name = models.CharField(max_length = 20)
    email = models.CharField(max_length = 50)
    address = models.CharField(max_length = 200)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length = 15)
    user_name = models.IntegerField(default = 0)
    password = models.CharField(max_length = 40,default = '')
    company_name = models.CharField(max_length = 30)
    holder_name =  models.CharField(max_length = 30)
    ifsc = models.CharField(max_length = 50)
    branch = models.CharField(max_length = 50)
    account_number = models.BigIntegerField()
    pic = models.ImageField(upload_to = 'seller/' ,default='static/images/defaulimage.png')
    status = models.CharField(max_length = 20, default = 'pending')

    class Meta:
        db_table = 'seller'