"""Final challenge views"""
from django.urls import path
#Consultas
from .views import query_one
from .views import query_two
from .views import query_three
from .views import query_four
from .views import query_five
from .views import query_six
from .views import query_seven
from .views import query_eight
from .views import query_nine

app_name = 'final_challenge'

urlpatterns = [
    path('query_one/', query_one, name='query_one'),
    path('query_two/', query_two, name='query_two'),
    path('query_three', query_three, name='query_three'),
    path('query_four/', query_four, name='query_four'),
    path('query_five/', query_five, name='query_five'),
    path('query_six/', query_six, name='query_six'),
    path('query_seven/', query_seven, name='query_seven'),
    path('query_eight/', query_eight, name='query_eight'),
    path('query_nine/', query_nine, name='query_nine'),
]
