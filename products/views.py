from django.shortcuts import render


def all_products(request):
    """ Aview to show products """
    return render(request, 'products/products.html')
