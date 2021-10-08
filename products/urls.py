from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new_products),
    path('new/xx1', views.new_pro1)
]
