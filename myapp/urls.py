from atexit import register
from typing import Counter
from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    
    path('register', views.register, name ='register'),
    path('login', views.login, name ='login'),
    path('logout', views.logout, name ='logout'),
    path('prices', views.prices, name ='prices'),
    path('test2', views.test, name = 'test'),
    path('upload', views.upload, name ='upload'),
    path('gallery', views.gallery, name='gallery'),
    path('photo/<str:primary_key>/', views.viewPost, name='photo')
]



