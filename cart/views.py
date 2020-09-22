from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from coupons.models import Coupon


def cart(request):
    """ returns shopping cart page """
    return render(request, 'cart/cart.html')

@property #if cart contains coupon, coupon object with id is returned
def cart_coupon(self):
    if self.coupon_id:
        return Coupon.objects.get(id=self.coupon_id)
    return None

#retrieve discount rate
def get_discount(self):
    if self.coupon:
        return(self.coupon.discount / Decimal('100')) *self.grand_total
        return Decimal('0')


def get_price_after_discount(self):
    return self.grand_total() - self.get_discount()


def update_cart(request, selected_item_id):
    quantity = int(request.POST.get('quantity'))
    weight = float(request.POST.get('weight'))
    remove = request.POST.get('remove')
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', [])
    coupon = request.session.get('coupon_id')

    if len(cart) > 0:
        for index, (item_id, item_weight, item_quantity) in enumerate(cart):

            if item_id == selected_item_id and item_weight == weight:
                if quantity == 0 or remove:
                    del cart[index]
                else:
                    messages.success(request, "Item Added To Your Cart!")
                    cart[index] = (item_id, item_weight, quantity)
                    
            else:
                messages.success(request, "Item Added To Your Cart!")
                cart.append((selected_item_id, weight, quantity))
    else:
        messages.success(request, "Item Added To Your Cart!")
        cart.append((selected_item_id, weight, quantity))
        
    request.session['cart'] = cart
    request.session['coupon_id'] = coupon
    
    if redirect_url:
        return redirect(redirect_url)
    return redirect(reverse('cart'))



