from django.shortcuts import render, redirect, reverse
from django.contrib import messages


def cart(request):
    """ returns shopping cart page """

    return render(request, 'cart/cart.html')


def update_cart(request, selected_item_id):
    quantity = int(request.POST.get('quantity'))
    weight = float(request.POST.get('weight'))
    remove = request.POST.get('remove')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', []) 
    
    if len(cart) > 0:
        for index, (item_id, item_weight, item_quantity) in enumerate(cart):

            if item_id == selected_item_id and item_weight == weight:
                if quantity == 0 or remove:
                    del cart[index]
                    messages.success(request, "Item Removed From Cart")
                else:
                    messages.success(request, "Item Added!")
                    cart[index] = (item_id, item_weight, quantity)
                    
            else:
                messages.success(request, "Item Added To Your Cart!")
                cart.append((selected_item_id, weight, quantity))
    else:
        messages.success(request,  "Item Added To Your Cart!")
        cart.append((selected_item_id, weight, quantity))
    
    request.session['cart'] = cart
   
    if redirect_url:
        return redirect(redirect_url)
    return redirect(reverse('cart'))



