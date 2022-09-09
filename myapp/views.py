from random import randint
import re
from unicodedata import category
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import ApprovalForm
from .models import Feature, UserExtend, Store, VolunteeringOption, Category, ApprovalToConfirm, UserApproval
from datetime import datetime




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
                extendedUser.coins = 0
                extendedUser.save()
                return redirect('login')
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

        try:
            user2 = User.objects.get(email__exact=username)
            user_by_mail = auth.authenticate(username=user2.username, password=password)
        except:
            messages.info(request, 'Credentials invalid')
            return redirect('login')

        if user_by_mail is not None:
            auth.login(request, user_by_mail)
            return redirect('/')
        else:
            messages.info(request, 'Credentials invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def gallery(request):
    extendedUsers = UserExtend.objects.all()
    categories = Category.objects.all()
    posts = posts = VolunteeringOption.objects.filter(is_approved=True)

    if request.method == 'POST':
        category = request.POST.get('categories')
        print(category)
        if category == 'All':
            if request.POST.get('price'):
                posts = VolunteeringOption.objects.filter(is_approved=True).order_by('value').reverse()
            elif request.POST.get('name'):
                posts = VolunteeringOption.objects.filter(is_approved=True).order_by('full_name')
            else:
                posts = VolunteeringOption.objects.filter(is_approved=True)

            context = {'categories': categories, 'posts': posts, 'extendedUsers': extendedUsers, }
            return render(request, 'templates/gallery.html', context)

        else:
            if request.POST.get('price'):
                posts = VolunteeringOption.objects.filter(category__name=category, is_approved=True).order_by(
                    'value').reverse()
            elif request.POST.get('name'):
                posts = VolunteeringOption.objects.filter(category__name=category, is_approved=True).order_by(
                    'full_name')
            else:
                posts = VolunteeringOption.objects.all().filter(category__name=category, is_approved=True)
            context = {'categories': categories, 'posts': posts, 'extendedUsers': extendedUsers, }
            return render(request, 'templates/gallery.html', context)

    context = {'categories': categories, 'posts': posts, 'extendedUsers': extendedUsers}
    return render(request, 'templates/gallery.html', context)


def prices(request):
    stores = Store.objects.all()
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

    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    coupon_code = randint(1000000000, 9999999999)
    if request.method == 'POST':
        userInput = request.POST.get("userInput")

    if request.POST.get('btn1') and connected and userInput == 'True':
        if extended.coins - 20 >= 0:
            extended.coins = extended.coins - 20
            extended.add_coupon({coupon_code: 123})
            extended.add_date({date_time: 123})
            extended.add_store({'1': 123})
            extended.save()
        return render(request, 'templates/prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
                                                         'store2': store2, 'store3': store3, 'store4': store4,
                                                         'extended': extended})

    if request.POST.get('btn2') and connected and userInput == 'True':
        if extended.coins - 10 >= 0:
            extended.coins = extended.coins - 10
            extended.add_coupon({coupon_code: 123})
            extended.add_date({date_time: 123})
            extended.add_store({'2': 123})
            extended.save()
        return render(request, 'templates/prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
                                                         'store2': store2, 'store3': store3, 'store4': store4,
                                                         'extended': extended})

    if request.POST.get('btn3') and connected and userInput == 'True':
        if extended.coins - 50 >= 0:
            extended.coins = extended.coins - 50
            extended.add_coupon({coupon_code: 123})
            extended.add_date({date_time: 123})
            extended.add_store({'3': 123})
            extended.save()
        return render(request, 'templates/prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
                                                         'store2': store2, 'store3': store3, 'store4': store4,
                                                         'extended': extended})

    if request.POST.get('btn4') and connected and userInput == 'True':
        if extended.coins - 100 >= 0:
            extended.coins = extended.coins - 100
            extended.add_coupon({coupon_code: 123})
            extended.add_date({date_time: 123})
            extended.add_store({'4': 123})
            extended.save()
        return render(request, 'templates/prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
                                                         'store2': store2, 'store3': store3, 'store4': store4,
                                                         'extended': extended})

    if request.user.is_authenticated:
        return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
                                               'store2': store2, 'store3': store3, 'store4': store4,
                                               'extended': extended})

    return render(request, 'prices.html', {'extendedUsers': extendedUsers, 'store1': store1,
                                           'store2': store2, 'store3': store3, 'store4': store4})


def uploadApproval(request, primary_key):
    post = VolunteeringOption.objects.get(id=primary_key)
    user = request.user
    extendedUsers = UserExtend.objects.all()
    for e in extendedUsers:
        if e.user.username == user.username:
            extended = e
    form = ApprovalForm()

    if request.method == 'POST':

        form = ApprovalForm(request.POST, request.FILES)
        extended = UserExtend.objects.get(pk=extended.id)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = extended
            form.value = post.value
            form.save()

            user_approval = UserApproval(date=datetime.now(), description=form.description, image=form.image,
                                         is_approved=None, value=form.value, user=form.user, pk=form.pk)
            user_approval.save()
        return redirect('/')

    context = {'form': form, 'extended': extended, 'extendedUsers': extendedUsers}
    return render(request, 'upload_approval.html', context)


def viewPost(request, primary_key):
    extendedUsers = UserExtend.objects.all()
    post = VolunteeringOption.objects.get(id=primary_key)
    return render(request, 'photo.html', {'post': post, 'extendedUsers': extendedUsers})


def myCoupons(request):
    stores = Store.objects.all()
    list_stores = list(stores)
    store1 = list_stores[0]
    store2 = list_stores[1]
    store3 = list_stores[2]
    store4 = list_stores[3]
    extendedUsers = UserExtend.objects.all()
    user = request.user
    for e in extendedUsers:
        if e.user.username == user.username:
            extended = e

    if (extended.coupons_counter):
        coupons_list = zip(extended.get_coupons_list(), extended.get_date_list(), extended.get_store_list())
        context = {'coupons_list': coupons_list, 'store1': store1, 'store2': store2, 'store3': store3, 'store4': store4,
                   'extended': extended, 'extendedUsers': extendedUsers}
        return render(request, 'mycoupons.html', context, )

    context = {'coupons_list': [], 'store1': store1, 'store2': store2, 'store3': store3, 'store4': store4,
               'extended': extended, 'extendedUsers': extendedUsers}
    return render(request, 'mycoupons.html', context, )


def about(request):
    stores = Store.objects.all()
    list_stores = list(stores)
    store1 = list_stores[0]
    store2 = list_stores[1]
    store3 = list_stores[2]
    store4 = list_stores[3]
    extendedUsers = UserExtend.objects.all()
    if request.POST.get('btn1'):
        return redirect('register')

    return render(request, 'about.html', {'extendedUsers': extendedUsers, 'store1': store1,
                                          'store2': store2, 'store3': store3, 'store4': store4})


def adminViewApprovals(request):
    approvals = ApprovalToConfirm.objects.all()
    extendedUsers = UserExtend.objects.all()

    if not request.user.is_authenticated:
        redirect('login')
    user = request.user
    if user.username != 'admin':
        return redirect('/')

    if request.method == 'POST':
        for e in extendedUsers:
            if e.user.username == user.username:
                extended = e
        for approval in approvals:
            if request.POST.get(str(approval.id)) != None:
                realApproval = ApprovalToConfirm.objects.get(pk=approval.id)
                realApproval.user.coins += approval.value
                realApproval.user.save()
                approvalPost = UserApproval.objects.get(id=realApproval.id)
                approvalPost.is_approved = realApproval.is_approved
                approvalPost.save()
                realApproval.delete()
                approvals = ApprovalToConfirm.objects.all()
                return render(request, 'admin_view_approvals.html',
                              {'approvals': approvals, 'extendedUsers': extendedUsers})

        for approval in approvals:
            if request.POST.get(str(-approval.id)) != None:
                realApproval = ApprovalToConfirm.objects.get(pk=approval.id)
                realApproval.delete()

                approvals = ApprovalToConfirm.objects.all()
                return render(request, 'admin_view_approvals.html',
                              {'approvals': approvals, 'extendedUsers': extendedUsers})

    return render(request, 'admin_view_approvals.html', {'approvals': approvals, 'extendedUsers': extendedUsers})


def uploadVolunteerOption(request):
    categories = Category.objects.all()
    extendedUsers = UserExtend.objects.all()
    if request.method == "POST":
        full_name = request.POST.get('association')
        address = request.POST.get('address')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        category_name = request.POST.get('categories')
        value = request.POST.get('coins')

        for category in categories:
            if category.name == category_name:
                real_category = category
        post = VolunteeringOption(full_name=full_name, address=address, city=city, phone_number=phone_number,
                                  category=real_category,
                                  image=image, description=description, is_approved=False, value=value)
        post.save()

    return render(request, 'upload_volunteer_option.html', {'categories': categories, 'extendedUsers': extendedUsers})


def adminViewVolunteeringRequests(request):
    posts = VolunteeringOption.objects.filter(is_approved=False)
    extendedUsers = UserExtend.objects.all()
    if not request.user.is_authenticated:
        redirect('login')
    user = request.user
    if user.username != 'admin':
        return redirect('/')

    if request.method == 'POST':
        for post in posts:
            if request.POST.get(str(post.id)) != None:
                realPost = VolunteeringOption.objects.get(pk=post.id)
                realPost.is_approved = True
                realPost.save()
                posts = VolunteeringOption.objects.filter(is_approved=False)
                return render(request, 'admin_view_volunteering_requests.html',
                              {'posts': posts, 'extendedUsers': extendedUsers})

        for post in posts:
            if request.POST.get(str(-post.id)) != None:
                realPost = VolunteeringOption.objects.get(pk=post.id)
                realPost.delete()
                posts = VolunteeringOption.objects.filter(is_approved=False)
                return render(request, 'admin_view_volunteering_requests.html',
                              {'posts': posts, 'extendedUsers': extendedUsers})

    return render(request, 'admin_view_volunteering_requests.html', {'posts': posts, 'extendedUsers': extendedUsers})


def adminViewExistingPosts(request):
    posts = VolunteeringOption.objects.filter(is_approved=True)
    extendedUsers = UserExtend.objects.all()
    if not request.user.is_authenticated:
        redirect('login')
    user = request.user
    if user.username != 'admin':
        return redirect('/')

    if request.method == 'POST':
        for post in posts:
            if request.POST.get(str(post.id)) != None:
                realPost = VolunteeringOption.objects.get(pk=post.id)
                realPost.delete()
                posts = VolunteeringOption.objects.filter(is_approved=True)
                return render(request, 'admin_view_existing_posts.html',
                              {'posts': posts, 'extendedUsers': extendedUsers})

    return render(request, 'admin_view_existing_posts.html', {'posts': posts, 'extendedUsers': extendedUsers})


def myApprovals(request):
    extendedUsers = UserExtend.objects.all()
    approvedPosts = UserApproval.objects.all()
    for e in extendedUsers:
        if e.user.username == request.user.username:
            extended = e
    approvedPostsFiltered = approvedPosts.filter(user=extended)

    if request.method == "POST":
        if request.POST.get('price'):
            approvedPostsFiltered = approvedPostsFiltered.order_by('value').reverse()
        elif request.POST.get('date'):
            approvedPostsFiltered = approvedPostsFiltered.order_by('date')
        elif request.POST.get('approved'):
            approvedPostsFiltered = approvedPostsFiltered.filter(is_approved=True)

        return render(request, 'templates/my_approvals.html',
                      {'approvedPostsFiltered': approvedPostsFiltered, 'extendedUsers': extendedUsers})

    return render(request, 'templates/my_approvals.html',
                  {'approvedPostsFiltered': approvedPostsFiltered, 'extendedUsers': extendedUsers})
