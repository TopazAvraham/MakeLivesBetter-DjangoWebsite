from datetime import timezone
from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField,ImageField,ManyToManyField,BooleanField,\
    IntegerField,OneToOneField,ForeignKey,DateField


# Create your models here.
class Feature(models.Model):
    name = CharField(max_length=100)

    details = CharField(max_length=400)
    icon = ImageField(upload_to="files/", null=True, blank=True)

    def __str__(self):
        return self.name


class UserExtend(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE)
    coins = IntegerField()
    coupons_list = CharField(max_length=1000000, null=True, blank=True)
    coupons_counter = IntegerField(default=0)
    date_list = CharField(max_length=1000000, null=True, blank=True)
    store_list = CharField(max_length=1000000, null=True, blank=True)
    approvals = ForeignKey('ApprovedPost',on_delete=models.SET_NULL, null=True, blank=True)

    # approvals = ForeignKey('Approval',on_delete=models.SET_NULL, null=True, blank=True)
    def add_coupon(self, data):
        if self.coupons_list is None:
            self.coupons_list = '.'.join(map(str, data))
            self.coupons_counter = 1
        else:
            self.coupons_list += ('.' + '.'.join(map(str, data)))
            self.coupons_counter = self.coupons_counter + 1

    def get_coupons_list(self):
        return list(map(str, self.coupons_list.split('.')))

    def add_date(self, data):
        if self.date_list is None:
            self.date_list = '.'.join(map(str, data))
        else:
            self.date_list += ('.' + '.'.join(map(str, data)))

    def get_date_list(self):
        return list(map(str, self.date_list.split('.')))

    def add_store(self, data):
        if self.store_list is None:
            self.store_list = '.'.join(map(str, data))
        else:
            self.store_list += ('.' + '.'.join(map(str, data)))

    def get_store_list(self):
        return list(map(str, self.store_list.split('.')))

    def __str__(self):
        return self.user.username


class Stores(models.Model):
    name = CharField(max_length=100)
    product = CharField(max_length=100)
    logo = ImageField(upload_to="files/", null=True, blank=True)
    id_number = CharField(blank=True, default=0, max_length=100)
    product_photo = ImageField(upload_to="files/", null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    full_name = CharField(max_length=100)
    address = CharField(max_length=100)
    city = CharField(max_length=100)
    phone_number = CharField(max_length=10)
    is_approved = BooleanField(default=False)
    category = ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = CharField(blank=True, max_length=224, null=True)
    image = ImageField(upload_to="files/", null=False, blank=False)
    value = IntegerField(blank=True, default=0)

    def __str__(self):
        return self.full_name



class Approval(models.Model):
    user = ForeignKey(UserExtend, on_delete=models.SET_NULL, null=True, blank=True)
    date = DateField(default=date.today)
    description = CharField(blank=True, max_length=250, null=True)
    image = ImageField(upload_to="files/", null=True, blank=True)
    is_approved = BooleanField()
    value = IntegerField(blank=True, default=0)

    def __str__(self):
        return str(self.user)

class ApprovedPost(models.Model):
    date = DateField(default=date.today)
    description = CharField(blank=True, max_length=250, null=True)
    image = ImageField(upload_to="files/", null=True, blank=True)
    is_approved = BooleanField(default=None, blank=True, null=True)
    value = IntegerField(blank=True, default=0)
    user = ForeignKey(UserExtend, on_delete=models.SET_NULL, null=True, blank=True)
