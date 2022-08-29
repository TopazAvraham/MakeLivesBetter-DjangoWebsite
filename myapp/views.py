from distutils.file_util import move_file
from email.mime import image
from random import randint, random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature, UserExtend, Stores, Post
from django.db.models import F
from django.shortcuts import get_object_or_404
from django.http import Http404
from .form import ImageForm


# Create your views here.
def index(request):
    features = Feature.objects.all()
    extendedUsers = UserExtend.objects.all()
    return render(request, 'index.html', {'features': features, 'extendedUsers': extendedUsers})

def counter(request):
    posts = [1,2,3,4,5, 'tim', 'tom', 'john']
    return render(request, 'counter.html', {'posts': posts})

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

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})

def prices(request):
    stores = Stores.objects.all()
    list_stores = list(stores)
    store1 = list_stores[0]
    store2 = list_stores[1]
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
        return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1, 'store2': store2, 'extended': extended})
        
    if request.POST.get('btn2') and connected:
        if extended.coins - 10 >= 0:
            extended.coins = extended.coins - 10
            extended.save()
        return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1, 'store2': store2, 'extended': extended})
    
    if request.user.is_authenticated:
        return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1, 'store2': store2, 'extended': extended})
    
    return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1, 'store2': store2})

def test(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            
            return render(request,"index.html",{"obj":obj})
        else:
            form=ImageForm()
        img=Post.objects.all()
        return render(request,"index.html",{"img":img,"form":form})
    return render(request, 'index2.html')

def upload(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        full_name= request.POST['full_name']
        address= request.POST['address']
        city= request.POST['city']
        phone_number= request.POST['phone_number']
        image = request.POST['image']
        post = Post.objects.create(full_name=full_name,address=address,city=city,phone_number=phone_number, is_approved = True, image=image )
        post.save()
        return redirect('index')   
    else:
        return render(request, 'upload.html')


def search(request):
    posts = Post.objects.all()
    
    return render(request, 'search.html', {'posts': posts})
    




