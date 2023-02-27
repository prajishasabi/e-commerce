from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    gender = models.CharField(max_length = 10)
    phone = models.BigIntegerField()
    user_name = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20) 

    class Meta:
        db_table = 'student'
    