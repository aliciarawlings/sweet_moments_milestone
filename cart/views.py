from django.shortcuts import render


def cart(request):
    """ returns shopping cart page """
    return render(request, 'cart/cart.html')
