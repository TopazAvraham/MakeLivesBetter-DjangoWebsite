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


# Create your views here.
def index(request):
    features = Feature.objects.all()
    extendedUsers = UserExtend.objects.all()
    return render(request, 'newIndex.html', {'features': features, 'extendedUsers': extendedUsers})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

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
                extendedUser.coins = randint(0, 9)
                extendedUser.save()
                return redirect('index')
        else:
            messages.info(request, 'Passwords don\'t match')
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

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
    return render(request, 'newIndex.html', {'features': features, 'extendedUsers': extendedUsers})


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
                                               'store2': store2, 'store3': store3, 'store4': store4,
                                               'extended': extended})

    if request.POST.get('btn2') and connected:
        if extended.coins - 10 >= 0:
            extended.coins = extended.coins - 10
            extended.save()
        return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
                                               'store2': store2, 'store3': store3, 'store4': store4,
                                               'extended': extended})

    if request.POST.get('btn3') and connected:
        if extended.coins - 50 >= 0:
            extended.coins = extended.coins - 50
            extended.save()
        return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
                                               'store2': store2, 'store3': store3, 'store4': store4,
                                               'extended': extended})

    if request.POST.get('btn4') and connected:
        if extended.coins - 100 >= 0:
            extended.coins = extended.coins - 100
            extended.save()
        return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
                                               'store2': store2, 'store3': store3, 'store4': store4,
                                               'extended': extended})

    if request.user.is_authenticated:
        return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
                                               'store2': store2, 'store3': store3, 'store4': store4,
                                               'extended': extended})

    return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
                                           'store2': store2, 'store3': store3, 'store4': store4})


def upload(request, primary_key):
    if not request.user.is_authenticated:
        return redirect('login')
    post = Post.objects.get(id=primary_key)

    if request.method == 'POST':
        extendedUsers = UserExtend.objects.all()
        check = request.user.username
        for e in extendedUsers:
            if e.user.username == check:
                extended = e
        extended.coins += post.value
        extended.save()
        return redirect('/')

    categories = Category.objects.all()

    return render(request, 'upload.html', {'categories': categories})


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
