
from pyexpat.errors import messages
import re
from django.shortcuts import render
from urllib.request import Request
from django.contrib.auth.models import User 
from re import X
from .models import register

# from mystore.mysite.models import Category

from mysite.models import Info 

# Create your views here.



def index(request):
    
    ## load all users
    ## send the user details to the template
    users = User.objects.all()
    
    return render(request,'index.html',{'users':users})


def form(request):
    if request.method == 'POST':    
        
        Country = request.POST.get('Country')
        City = request.POST.get('City')
        street = request.POST.get('street')
       

        data = Info(Country=Country,City=City,street=street)  
        data.save()
        # data=Info.objects.create(Country=Country,City=City,street=street)
        # data.create()
        messages.success(request,'Data has been submitted')
    
    return render(request, 'index.html')






# def cat(request):
#     if request.method == 'POST':    
        
#         Description = request.POST.get(' Description')
      
       

#         data = Category( Description=Description)
#         data.save()
    
#     return render(request, 'index.html')






# def pro(request):
#     if request.method == 'POST':    
        
#         name1 = request.POST.get(' name1')
#         image = request.POST.get(' image')
#         Sku = request.POST.get(' Sku')
#         price = request.POST.get(' price')
#         category_id= request.POST.get('category_id')

#         data = pro( name1=name1,image=image,Sku=Sku,price=price,category_id=category_id)
#         data.save()
    
#     return render(request, 'index.html')







def registration(request):
    if request.method=="POST":
        post=register()
        post.name=request.POST['name']
        post.email=request.POST['email']
        post.phone=request.POST['phone']
        post.address=request.POST['address']
        post.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')

























































































































































































