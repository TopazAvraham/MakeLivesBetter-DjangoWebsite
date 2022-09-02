from email.policy import default
from pydoc import describe

from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)

    details= models.CharField(max_length=400)
    icon = models.ImageField(upload_to = "files/", null=True, blank=True)



class UserExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.IntegerField()
    coupons_list = models.CharField(max_length=1000000, null=True, blank=True)
    coupons_counter = models.IntegerField(default=0)
    date_list = models.CharField(max_length=1000000, null=True, blank=True)

    def add_coupon(self,data):
        if self.coupons_list is None:
            self.coupons_list = '.'.join(map(str, data))
            self.coupons_counter = 1
        else:
            self.coupons_list +=  ('.' + '.'.join(map(str, data)))
            self.coupons_counter = self.coupons_counter +1

    def get_coupons_list(self):
        return list(map(str, self.coupons_list.split('.')))

    def add_date(self,data):
        if self.date_list is None:
            self.date_list = '.'.join(map(str, data))
        else:
            self.date_list +=  ('.' + '.'.join(map(str, data)))

    def get_date_list(self):
        return list(map(str, self.date_list.split('.')))

    

class Stores(models.Model):
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="files/", null=True, blank=True)


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    is_approved = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(blank=True, max_length=1000, null=True)
    image = models.ImageField(upload_to="files/", null=False, blank=False)
    value = models.IntegerField(blank=True,default= 0)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

