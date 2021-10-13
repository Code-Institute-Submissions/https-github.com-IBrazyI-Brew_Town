from django.shortcuts import render

def view_all_products(request):
    return render(request, 'products/products.html')
