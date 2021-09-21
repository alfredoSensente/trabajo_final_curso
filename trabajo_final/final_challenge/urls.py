"""Final challenge views"""
from django.urls import path
from .views import index, hello_user

urlpatterns = [
    path('index/', index, name='index'),
    path('hello/', hello_user, name='hello'),
]
