from django.contrib import admin
from .models import Products, Category


class ProductsAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',

    )
    ordering = ('sku',)


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category)

