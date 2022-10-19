
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
    
    return render(request,'index.html',{'users':users})




def cat(request):
    
    if request.method == 'POST':
        Description=request.POST['Description']

        data=Category(Description=Description)
        data.save()


    return render(request,'index.html')




def prod(request):

    if request.method == 'POST':
        name1= request.POST[' name1']
        image= request.POST['image']
        Sku=request.POST['Sku']
        price=request.POST['price']
        category_id=request.POST[' category_id']


        data=pro(name1=name1, image=image, Sku= Sku, price=price, category_id=category_id)
        data.save()


    return render(request,'index.html')
































































































































































































