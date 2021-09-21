from django.shortcuts import render
from django.http import HttpResponse
from .services import get_username

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the final challenge index.")

def hello_user(requests):
    context = {
        'name': get_username()
    }
    return render(requests, 'final_challenge/hello_user.html', context)
