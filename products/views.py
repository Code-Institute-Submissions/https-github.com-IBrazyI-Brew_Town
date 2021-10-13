from django.shortcuts import render

def view_all(request):
    return render(request, 'products/products.html')
