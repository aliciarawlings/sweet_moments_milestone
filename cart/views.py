from django.shortcuts import render, redirect, reverse


def cart(request):
    """ returns shopping cart page """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    
    if item_id in list(cart.keys()):
        cart[item_id] += quantity

    else:
        cart[item_id] = quantity
    
    request.session['cart'] = cart
    return redirect(redirect_url)


def update_cart(request, item_id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 1:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)
    
    request.session['cart'] = cart
    return redirect(reverse('cart'))
    