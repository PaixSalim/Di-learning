from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    ADMIN ='ADMIN'
    CUSTOMER= 'CUSTONER'
    
    ROLE = [(ADMIN,'Admin'),(CUSTOMER,'CUSTOMER')]
    name= models.CharField(max_length=30)
    number = PhoneNumberField()