from importlib.resources import path
from django.urls import path , include
from mysite import views
from . import views

from django.urls import path, include
from django.contrib.auth import views as auth_views


 
# define the router path and viewset to be used


urlpatterns = [
   path('',views.index),
   path('category',views.cat),
   path('product',views.prod),
   path('info',views.info),
   path('categoryGet',views.categoryGet),
   path('register', views.UserCreate.as_view()),
   path('products',views.ProductsApi.as_view()),

  
  
   
   
   
   
  
   


   
  
   
   
   
   
 

   
   
]




