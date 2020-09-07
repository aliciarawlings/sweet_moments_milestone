from django.shortcuts import render, get_object_or_404
from .models import Products


def all_products(request):
    """ A view to show products """
 
    products = Products.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, products_id):
    """ A view to show product details """
 
    product = get_object_or_404(Products, pk=products_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)