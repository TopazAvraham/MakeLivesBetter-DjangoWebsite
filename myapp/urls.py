from atexit import register
from typing import Counter
from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('prices', views.prices, name='prices'),
    path('upload_approval/<str:primary_key>/', views.uploadApproval, name='upload_approval'),
    path('photo/<str:primary_key>/', views.viewPost, name='photo'),
    path('mycoupons', views.myCoupons, name='mycoupons'),
    path('about', views.about, name = 'about'),
    path('gallery', views.gallery, name='gallery'),
    path('admin_view_approvals', views.adminViewApprovals, name='admin_view_approvals'),
    path('upload_volunteer_option', views.uploadVolunteerOption, name='upload_volunteer_option'),
    path('admin_view_volunteering_requests', views.adminViewVolunteeringRequests, name='admin_view_volunteering_requests'),
    path('admin_view_existing_posts', views.adminViewExistingPosts, name='admin_view_existing_posts'),
    path('myapprovals', views.myapprovals, name='myapprovals')]
