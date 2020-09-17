from django.shortcuts import render, redirect, reverse


def cart(request):
    """ returns shopping cart page """
    return render(request, 'cart/cart.html')

# selected_items = [item for item in cart if item[0] == selected_item_id]

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
                else:
                    cart[index] = (item_id, item_weight, quantity)
            else:
                cart.append((selected_item_id, weight, quantity))
    else:
        cart.append((selected_item_id, weight, quantity))

    request.session['cart'] = cart
    if redirect_url:
        return redirect(redirect_url)
    return redirect(reverse('cart'))

# def delete_cart_item(request, item_id):
#     cart = request.session.get('cart', {})
#     item_id = get_object_or_404(Product, id=product_id)
#     cart.remove(item_id)
#     return redirect(reverse('cart'))
