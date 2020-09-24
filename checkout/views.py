from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
from coupons.models import Coupon


def checkout(request):
    cart = request.session.get('cart', {})
    coupon = request.session.get('coupon_id', {})
    
    if not cart:
        messages.error(request, "oops your bag is empty")
        return redirect(reverse('products'))
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    
    context = {
     'order_form':order_form,
     'coupon':coupon,
     'stripe_public_key':'pk_test_51HIB0uIgPE9MtcG4L1wBF3rLiVin1wscx39uHFjELOWHfd7TF0jMJhl978Sbzz84iTzgf9ntgKXDVLniGOccpyFx00xIuoHzZU',
      
    } 
    return render(request, template, context)


