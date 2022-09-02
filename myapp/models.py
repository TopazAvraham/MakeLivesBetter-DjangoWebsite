from email.policy import default
from pydoc import describe

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details= models.CharField(max_length=400)
    icon = models.ImageField(upload_to = "files/", null=True, blank=True)

class UserExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.IntegerField()
    coupons = models


class Stores(models.Model):
    name = models.CharField(max_length=100)
    product= models.CharField(max_length=100)
    logo = models.ImageField(upload_to = "files/", null=True, blank=True )



class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    #user = models.ForeignKey(
     #   User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    full_name = models.CharField(max_length=100)
    address= models.CharField(max_length=100)
    city= models.CharField(max_length=100)
    phone_number= models.CharField(max_length=10)
    is_approved = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(blank = True, max_length=1000, null=True)
    image= models.ImageField(upload_to = "files/", null=False, blank=False )
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    

