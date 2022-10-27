
from pyexpat.errors import messages
import re
from unicodedata import category
from unittest import skip
from urllib import response
from webbrowser import get
from django.shortcuts import render
from urllib.request import Request
from django.contrib.auth.models import User 
from re import X
from django.http import JsonResponse




from mysite.models import Info , Category , pro

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
    if request.method == 'GET':

        Category_id=request.GET.get('Category_id')

        # response = {
        # 'is_taken': 
        # }
     
        



        


    return pro.objects.filter(Category_id_id=Category_id).all()



   






















































































































































































