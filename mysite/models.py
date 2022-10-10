
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
   






   



