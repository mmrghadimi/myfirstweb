from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# Create your views here.

# /products -> index
def index(request):
    products = Product.objects.all()
    # return HttpResponse('Hello World')
    return render(request, 'index.html',
                  {'pro': products})


def new_products(request):
    return HttpResponse('New Products')


def new_pro1(request):
    return HttpResponse('New Pro XX1')
