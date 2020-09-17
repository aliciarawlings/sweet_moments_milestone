from django.shortcuts import get_object_or_404
from products.models import Products


def cart_items(request):
    items = []
    total = 0
    product_count = 0

    weights = Products.QUANTITY_CHOICES
    cart = request.session.get('cart', [])

    for (item_id, weight, quantity) in cart:
        product = get_object_or_404(Products, pk=item_id)
        weight_price = float(weight) * float(product.price)
        subtotal = float(quantity) * weight_price
        total += subtotal
        product_count += quantity
        for w in weights:
            if w[0] == weight:
                display_weight = w[1]

        items.append({
            'product': product,
            'price': weight_price,
            'weight': {
                'decimal': weight,
                'display': display_weight
            },
            'quantity': quantity,
            'subtotal': subtotal
        })

    context = {
        'items': items,
        'total': total,
        'product_count': product_count,
    }

    return context
