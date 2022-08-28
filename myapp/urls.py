from atexit import register
from typing import Counter
from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('counter', views.counter, name ='counter'),
    path('register', views.register, name ='register'),
    path('login', views.login, name ='login'),
    path('logout', views.logout, name ='logout'),
    path('post/<str:pk>', views.post, name = 'post'),
    path('prices', views.prices, name ='prices'),
    path('test', views.test, name = 'test'),
    path('upload', views.test, name ='upload'),
    path('search', views.search, name ='search')
]



