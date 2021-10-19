from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

def view_all_products(request):
    """ Renders the products page, displays the products model and handles all sorting and searching queries """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
        if not query:
            messages.error(request, "Please enter an item you would like to search.")
            return redirect(reverse('product'))

            queries = Q(names__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    products_all = {
        'products' : products,
        'search_term' : query,
        }

    return render(request, 'products/products.html', products_all)
