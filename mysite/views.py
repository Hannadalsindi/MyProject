
import genericpath
import json
from pyexpat.errors import messages
import re
from types import GenericAlias
from typing import Generic
from unicodedata import category
from unittest import skip
from urllib import response

from django.shortcuts import render
from urllib.request import Request
from django.contrib.auth.models import User 
from typing import Generic
from re import X
from django.http import JsonResponse
from django.http import HttpResponse
from django.core import serializers
from rest_framework.permissions import AllowAny
from rest_framework import generics


from mysite.models import Info , Category,  pro,GeeksModel
from mysite.serializers import UserSerializer

from rest_framework import viewsets
from .serializers import   ProductsSerializer
from .models import GeeksModel 








# Create your views here.



def index(request):
    
    
        
    ## load all users
    ## send the user details to the template
   
    
    
   
   
    
    return render(request,'index.html')




def cat(request):
    
    if request.method == 'POST':
        Description=request.POST['Description']

        data=Category(Description=Description)
        data.save()
    
    


    return render(request,'category.html')




def prod(request):

    if request.method == 'POST':
        
        product_name= request.POST['product_name']
        image= request.POST['image']
        Sku=request.POST['Sku']
        price=request.POST['price']
        Category_id=request.POST['Category_id']
        
       


        data=pro(product_name=product_name, image=image, Sku= Sku, price=price, Category_id_id=Category_id)
        data.save()

    category=Category.objects.all()


    Pro=pro.objects.all()
   


    return render(request,'product.html',{'pro':Pro,'category':category})






def info(request):
    if request.method == 'POST':    
        User_id= request.POST['User_id']
        Country = request.POST['Country']
        City = request.POST['City']
        street = request.POST['street']

        

        
        data = Info(User_id_id = User_id, Country=Country,City=City,street=street)  
        data.save()
    users = User.objects.all()


    return render(request,'info.html',{'users':users})







def categoryGet(request):
      if request.method == "GET":
      
        Category_id = request.GET.get("Category_id")
        products = pro.objects.filter(Category_id_id=Category_id).all()
       
        jsondata = serializers.serialize('json', products)

      return HttpResponse(jsondata, content_type='application/json')

      
    




class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )

   









class ProductsApi(generics.CreateAPIView):
    # define queryset
    queryset = pro.objects.all()
     
    # specify serializer to be used
    serializer_class = ProductsSerializer
























































































































































































