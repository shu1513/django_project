from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "hello/index.html")


def shu(request):
    return HttpResponse("Hi Shu")


def greet(request, name):
    return HttpResponse(f"hello {name}!")
