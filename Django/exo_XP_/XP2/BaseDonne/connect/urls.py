from django.contrib import admin
from .views import *
from django.urls import path,include

urlpatterns = [
     path('',index, name='index'),
     path('famille',famille, name='famille'),
     path('afficher<int:id>/',afficher , name='afficher' ),
     
]