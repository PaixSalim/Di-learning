from django import views
from django.urls import path,include
from .views import *

urlpatterns = [

    path('',home, name='home'),
    path('location',locations, name='locations'),
    path('inscrire',inscrire, name='inscrire'),
    path('location<int:id>/',afficher , name='afficher' ),
   
]