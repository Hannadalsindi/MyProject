
from pyexpat.errors import messages
import re
from unicodedata import category
from unittest import skip
from webbrowser import get
from django.shortcuts import render
from urllib.request import Request
from django.contrib.auth.models import User 
from re import X




from mysite.models import Info , Category , pro

# Create your views here.



def index(request):
    if request.method == 'POST':    
        User_id= request.POST['User_id']
        Country = request.POST['Country']
        City = request.POST['City']
        street = request.POST['street']

        

        
        data = Info(User_id_id = User_id, Country=Country,City=City,street=street)  
        data.save()
    
        
    ## load all users
    ## send the user details to the template
    users = User.objects.all()
    category=Category.objects.all()
    print(category)
    Pro=pro.objects.all()
   
   
    
    return render(request,'index.html',{'users':users,'category':category,'pro':Pro})




def cat(request):
    
    if request.method == 'POST':
        Description=request.POST['Description']

        data=Category(Description=Description)
        data.save()


    return render(request,'index.html')




def prod(request):

    if request.method == 'POST':
        
        product_name= request.POST['product_name']
        image= request.POST['image']
        Sku=request.POST['Sku']
        price=request.POST['price']
        Category_id=request.POST['Category_id']
        
       


        data=pro(product_name=product_name, image=image, Sku= Sku, price=price, Category_id_id=Category_id)
        data.save()
   


    return render(request,'index.html')
































































































































































































