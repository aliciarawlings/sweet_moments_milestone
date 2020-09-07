from django.contrib import admin
from .models import Product, Category, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',

    )
    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Order)
