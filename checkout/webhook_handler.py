from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from checkout.models import Order, OrderItem
from products.models import Products

import json
import time


class StripeWH_Handler:
    """handles stripes Webhooks"""
    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """ used for unexpected webhook events"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)


def handle_payment_intent_succeeded(self, event):
    """ shows payment intent is successful webhook from stripe """
    intent = event.data.object
    pid= intent.id
    cart = intent.metadata.cart

    shipping_details = intent.shipping
    billing_details= intent.charges.data[0].billing_details
    grand_total = round(intent.data.charges[0].amount / 100, 2)

    order_recorded = False
    attempt = 1
    while attempt <= 5:
        try:
            order = Order.objects.get(
                first_name__iexact=shipping_details.first_name,
                second_name__iexact=shipping_details.second_name,
                telephone__iexact= shipping_details.telephone,
                email__iexact= shipping_details.email,
                address_1__iexact= shipping.details.address_1,
                address_2__iexact= shipping.details.address_2,
                county__iexact= shipping.details.county,
                country__iexact= shipping.details.country,
                grand_total=grand_total,
                original_cart=cart,
                stripe_pid=pid,
            )
            order_recorded = True
            break
        except Order.DoesNotExist:
            attempt += 1
            time.sleep(1)
    if order_recorded:
        return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Order in database',
                status=200)
    else:
        order = None
        try:
            order = Order.objects.create(
                first_name=shipping_details.first_name,
                second_name=shipping_details.second_name,
                telephone= shipping_details.telephone,
                email= shipping_details.email,
                address_1= shipping_details.address_1,                    address_2= shipping_details.address_2,
                county= shipping_details.county,                        country= shipping_details.country,
                original_cart=cart,
                stripe_pid=pid,
            )
            for (item_id, weight, quantity) in json.loads(cart).items():
                products = get_object_or_404(Products, pk=item_id)
                orderitem = OrderItem(
                    order=order,
                    products=products,
                    quantity=quantity
                )
                orderitem.save()
            
        except Exception as e:
            if order:
                order.delete()
                return HttpResponse(
                    content=f'Webhook received:{event["type"]} |ERROR: {e}',
                    status=500)
    return HttpResponse( 
        content=f'Webhook received:{event["type"]} |SUCCESS: created order in webhook'
        , status=200)


def handle_payment_intent_failed(self, event):
    return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
        