"""Final challenge views"""
from django.urls import path
from .views import index, hello_user, query_four

urlpatterns = [
    path('index/', index, name='index'),
    path('hello/', hello_user, name='hello'),
    path('query_four/', query_four, name='query_four'),
]
