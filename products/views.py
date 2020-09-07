from django.shortcuts import render
from .models import Products


def all_products(request):
    """ A view to show products """
 
    products = Products.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)
