from importlib.resources import path
from django.urls import path , include
from mysite import views
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('',views.index),
   path('addAddress',views.cat),
   path('product',views.prod),
   
   
   
]