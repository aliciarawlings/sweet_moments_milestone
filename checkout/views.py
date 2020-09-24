from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from coupons.models import Coupon
from cart.contexts import cart_items

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    cart = request.session.get('cart', {})
    current_cart = cart_items(request)
    coupon = request.session.get('coupon', None)

    if not cart:
        messages.error(request, "oops your bag is empty")
        return redirect(reverse('products'))

    total = current_cart['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
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