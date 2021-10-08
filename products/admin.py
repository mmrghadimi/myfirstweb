from django.contrib import admin
from .models import Product, DiscountOffer


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class DiscountOfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount')


admin.site.register(Product, ProductAdmin)
admin.site.register(DiscountOffer, DiscountOfferAdmin)
