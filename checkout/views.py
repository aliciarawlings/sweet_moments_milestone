from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from cart.contexts import cart_items
from products.models import Products
from .models import OrderItem, Order
from profiles.forms import UserProfileForm
from profiles.models import UserPage
from django.contrib.auth.models import User
import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        print(stripe.api_key)
        stripe.PaymentIntent.modify(pid, metadata={
            'username': request.user,
            'cart': json.dumps(request.session.get('cart'))
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry , your payment was not successful')
        return HttpResponse(content=e, status=400)


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
            'county': request.POST['county'],
            'telephone': request.POST['telephone'],
        }
        order_form = OrderForm(form_info)
        if order_form.is_valid():
            user = User.objects.get(username=request.user)
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.buyer = user
            order.save()
            # iterate to create each bag item
            for (item_id, weight, quantity) in cart:
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
        stripe_total = round(total * 100)  # striperequires amount to beinteger
        stripe.api_key = stripe_secret_key   # set secret key on stripe
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
            payment_method_types=['card'],
        )  # create payment intent

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
            stripe_total = round(total * 100) # striperequires amount integer
            stripe.api_key = stripe_secret_key   # set secret key on stripe
            intent = stripe.PaymentIntent.create(   #create payment intent
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
                payment_method_types=['card'],
            )
        return render(request, template, context)


def checkout_success(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    if request.user.is_authenticated:
        profile = UserPage.objects.get(user=request.user)
        order.user_page = profile
        order.save()
        user_page_form = UserProfileForm(instance=profile)
        if user_page_form.is_valid():
            user_page_form.save()

    messages.success(request, f'Yipee! Order accepted!, Your order number is {order_number}')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
