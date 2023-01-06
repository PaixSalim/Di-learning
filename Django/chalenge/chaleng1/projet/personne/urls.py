from django import views
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',people, name='people'),
    path('people/<int:id>/',choi, name='choi'),
]