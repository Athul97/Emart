from django.db import models

# Create your models here.

class AdminLog(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=15)

class UserLog(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=25)

class UserSignup(models.Model):
    name         = models.CharField(max_length=25)
    phone_number = models.IntegerField()
    address      = models.CharField(max_length=25)
    userlog      = models.ForeignKey(UserLog,on_delete=models.CASCADE)

class Category(models.Model):
    category_name = models.CharField(max_length=25)
    description   = models.CharField(max_length=25)
    image         = models.FileField(upload_to='Category/')

class Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=25)
    category         = models.ForeignKey(Category,on_delete=models.CASCADE)

class Brand(models.Model):
    brand_name = models.CharField(max_length=25)
    subcat     = models.ForeignKey(Subcategory, on_delete = models.CASCADE)
    

