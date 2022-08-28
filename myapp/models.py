from email.policy import default
import string
from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details= models.CharField(max_length=100)

class UserExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.IntegerField()
    coupons = models


class Stores(models.Model):
    name = models.CharField(max_length=100)
    product= models.CharField(max_length=100)

class Post(models.Model):
    full_name = models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    phone_number= models.IntegerField()
    is_approved = models.BooleanField()
    image= models.ImageField(upload_to = "files/", default= 'defultl.jpg' )