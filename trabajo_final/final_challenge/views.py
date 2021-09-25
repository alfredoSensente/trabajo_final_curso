from django.shortcuts import render
from django.http import HttpResponse
from requests.api import get
from .services import get_query_four, get_username

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the final challenge index.")

def hello_user(requests):
    context = {
        'name': get_username()
    }
    return render(requests, 'final_challenge/templates/hello_user.html', context)

def query_four(requests):
    """"El total de personas que vieron cada pelicula en centroamerica"""
    context = {
        'query_four': get_query_four()
    }
    return render(requests, 'final_challenge/templates/table_four.html', context)
