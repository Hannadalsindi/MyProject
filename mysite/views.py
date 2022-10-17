
from pyexpat.errors import messages
import re
from unicodedata import category
from webbrowser import get
from django.shortcuts import render
from urllib.request import Request
from django.contrib.auth.models import User 
from re import X




from mysite.models import Info , Category

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































































































































































































