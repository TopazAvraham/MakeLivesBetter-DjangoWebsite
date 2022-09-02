from distutils.file_util import move_file
from email.mime import image
from random import randint, random
from unicodedata import category
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature, UserExtend, Stores, Post, Category
from django.db.models import F
from django.shortcuts import get_object_or_404
from django.http import Http404
from datetime import datetime
from random import random


# Create your views here.
def index(request):
    features = Feature.objects.all()
    extendedUsers = UserExtend.objects.all()
    return render(request, 'newIndex.html', {'features': features, 'extendedUsers': extendedUsers})

def register(request):
    if request.method == 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                extendedUser = UserExtend()
                extendedUser.user = user
                extendedUser.coins = randint(0,9)
                extendedUser.save()
                return redirect('index')
        else:
            messages.info(request, 'Passwords don\'t match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']

        user = auth.authenticate(username = username, password = password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def test(request):
    features = Feature.objects.all()
    extendedUsers = UserExtend.objects.all()
    user = request.user
    for e in extendedUsers:
        if e.user.username == user.username:
            extended = e
   
    extended.add_coupon({'123':123})
    extended.add_coupon({'456':123})
    now=datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    extended.add_date({date_time:123})
    extended.save()
    user_coupons = extended.get_coupons_list()
    user_dates = extended.get_date_list()
    

    return render(request, 'mycoupons.html', {'features': features, 'extendedUsers': extendedUsers,
     'user_coupons': user_coupons, 'user_dates': user_dates})

def prices(request):
    stores = Stores.objects.all()
    list_stores = list(stores)
    store1 = list_stores[0]
    store2 = list_stores[1]
    store3 = list_stores[2]
    store4 = list_stores[3]
    extendedUsers = UserExtend.objects.all()
    connected = False
    if request.user.is_authenticated:
        connected = True
        check = request.user.username
        for e in extendedUsers:
            if e.user.username == check:
                extended = e
        
    if request.POST.get('btn1') and connected:
        if extended.coins - 20 >= 0:
            extended.coins = extended.coins - 20
            extended.save()
        return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
         'store2': store2, 'store3': store3, 'store4': store4, 'extended': extended})
        
    if request.POST.get('btn2') and connected:
        if extended.coins - 10 >= 0:
            extended.coins = extended.coins - 10
            extended.save()
        return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
         'store2': store2, 'store3': store3, 'store4': store4, 'extended': extended})
    
    if request.POST.get('btn3') and connected:
        if extended.coins - 50 >= 0:
            extended.coins = extended.coins - 50
            extended.save()
        return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
         'store2': store2, 'store3': store3, 'store4': store4, 'extended': extended})

    if request.POST.get('btn4') and connected:
        if extended.coins - 100 >= 0:
            extended.coins = extended.coins - 100
            extended.save()
        return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
         'store2': store2, 'store3': store3, 'store4': store4, 'extended': extended})
    
    if request.user.is_authenticated:
        return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
     'store2': store2, 'store3': store3, 'store4': store4, 'extended': extended})

    
    return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
     'store2': store2, 'store3': store3, 'store4': store4})


def upload(request):
    extendedUsers = UserExtend.objects.all()
    if not request.user.is_authenticated:
       return redirect('login')

    
    categories = Category.objects.all()
    if request.method == 'POST':

        data = request.POST

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        
        
        full_name = request.POST['full_name']
        address = request.POST['address']
        city = request.POST['city']
        phone_number = request.POST['phone_number']
        image = request.FILES['image']
        description = request.POST['description']
        post = Post.objects.create(category=category,
                                   image=image, full_name=full_name, address=address, city=city,
                                   phone_number=phone_number, is_approved=True, description=description)

        post.save()
        return redirect('index')
    else:
        return render(request, 'upload.html', {'categories': categories, 'extendedUsers': extendedUsers})

    
def gallery(request):
    extendedUsers = UserExtend.objects.all()
    categories = Category.objects.all() 
    category = request.GET.get('category')

    if category != None:
        if request.GET.get('category') == 'All':
            posts = Post.objects.all() 
            categories = Category.objects.all()
            context = {'categories': categories, 'posts': posts, 'extendedUsers': extendedUsers}
        else:
            posts = Post.objects.filter(category__name=category, ) 
            context = {'categories': categories, 'posts': posts, 'extendedUsers': extendedUsers}
            return render(request, 'gallery.html', context)

    posts = Post.objects.all() 
    categories = Category.objects.all()
    context = {'categories': categories, 'posts': posts, 'extendedUsers': extendedUsers}
    return render(request, 'gallery.html', context)
    

def viewPost(request, primary_key):
    post = Post.objects.get(id=primary_key)
    return render(request, 'photo.html', {'post': post})


def gallery2(request):
    categories = Category.objects.all()
    
    posts = Post.objects.all()
    context = {'categories': categories, 'posts': posts}
    return render(request, 'gallery.html', context) 


def myCoupons(request):
    extendedUsers = UserExtend.objects.all()
    user = request.user
    for e in extendedUsers:
        if e.user.username == user.username:
            extended = e
    coupons_list = zip(extended.get_coupons_list(),extended.get_date_list())
    context = {
            'coupons_list': coupons_list,
        }
    return render(request, 'mycoupons.html', context)


