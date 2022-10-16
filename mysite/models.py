

from distutils.command import upload
from email.mime import image
from pyexpat import model
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User 




class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30, blank=True)
    dept = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="user")

    

    def __str__(self):
        return self.user.username
   



class Info(models.Model):
    id = models.AutoField(primary_key=True)
    User_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    Country = models.CharField(max_length=30, blank=True)
    City = models.CharField(max_length=30, blank=True)
    street = models.CharField(max_length=30, blank=True)

    



class Category(models.Model):
    id = models.AutoField(primary_key=True)
    Description= models.CharField(max_length=30, unique=True)








class pro(models.Model):
    name1 = models.CharField(max_length=30, blank=True)
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='img', default=0)
    Sku = models.CharField(max_length=30, unique=True, default=0 )
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0.00)
    category_id = models.ForeignKey(Category , on_delete=models.CASCADE, default='1')
   



 


 
class register(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=100)

    