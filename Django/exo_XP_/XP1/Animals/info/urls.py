from django import views
from django.urls import path,include
from .views import *

urlpatterns = [

    path('',index, name='index'),
    path('animal/<int:id>/',animal, name='animal'),
    path('famille/<int:id>/',famille, name='famille'),
   
]