from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from coupons.models import Coupon
from cart.contexts import cart_items
from products.models import Products
from .models import OrderItem, Order


import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('cart', {})
    current_cart = cart_items(request)
    coupon = request.session.get('coupon', None)

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        form_info = {
            'first_name': request.POST['first_name'],
            'second_name': request.POST['second_name'],
            'email': request.POST['email'],
            'address_1': request.POST['address_1'],
            'address_2': request.POST['address_2'],
            'country': request.POST['country'],
            'county' : request.POST['county'],
            'telephone': request.POST['telephone'],
            'coupon': request.POST['coupon']
        }
        order_form = OrderForm(form_info)
        if order_form.is_valid():
            order = order_form.save()
            for (item_id, weight, quantity) in cart: #iterate to create each bag item
                try:
                    products = get_object_or_404(Products, pk=item_id)
                    orderitem = OrderItem(
                        order=order,
                        products=products,
                        quantity=quantity
         
                    )
                    orderitem.save()
                except Products.DoesNotExist:
                    messages.error(request, (
                        "OOOPS, that product wasnt found, please contact customer support")
                    )
                    order.delete()
                    return redirect(reverse('cart'))
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "there was an error")
            print(order_form.errors)
            return redirect(reverse('cart'))
    else:
        if not cart:
            messages.error(request, "oops your bag is empty")
            return redirect(reverse('products'))

        total = current_cart['total']
        stripe_total = round(total * 100) # stripe requires amount to charge integer
        stripe.api_key = stripe_secret_key   # set secret key on stripe
        intent = stripe.PaymentIntent.create(   #create payment intent
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            payment_method_types=['card'],
        )
        
        order_form = OrderForm()
        if not stripe_public_key:
            messages.warning(request, 'Stripe Public key is missing ')
        template = 'checkout/checkout.html'

        context = {
            'total': total,
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'current_cart': current_cart,
            'client_secret': intent.client_secret,
            
        }

        if coupon:
            context['discount'] = coupon['discount']
            context['discountedTotal'] = total - context['discount']

        return render(request, template, context)
        
    
def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Yipee! Order accepted!, Your order number is {order_number}')

    if 'cart' in request.session:
        del request.session['cart']
    
    template = 'checkout/checkout_success.html'
    context = {
        order: order,

    }

    return render(request, template, context)


