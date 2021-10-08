from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# /products -> index
def index(request):
    return HttpResponse('Hello World')


def new_products(request):
    return HttpResponse('New Products')


def new_pro1(request):
    return HttpResponse('New Pro XX1')
