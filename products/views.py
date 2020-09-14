from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from .models import Products, Category


def all_products(request):
    """ A view to show products """
    products = Products.objects.all()
    query = None
    categories = None
    if request.GET:
        if request.GET['category']:
            category = request.GET['category']
            products = products.filter(category__flavour=category)
            categories = Category.objects.filter(flavour=category)		
        elif request.GET['q']:
            query = request.GET['q']
            if not query:
                messages.error(request, "oops! you didnt enter any search criteria")
                return redirect(reverse('products'))

                queries = Q(category__icontains=query) | Q(description__icontains=query)
                products = products.filter(queries)

    context = {
        'products': products,
        'search' : query,
        'sweet_categories': categories, 
    }
    return render(request, 'products/products.html', context)


def product_detail(request, products_id):
    """ A view to show product details """

    product = get_object_or_404(Products, pk=products_id)

    context = {
    'product': product,
    }
    return render(request, 'products/product_detail.html', context)

