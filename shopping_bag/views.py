from django.shortcuts import render

def view_bag(request):
    """Renders the shopping bag page, will also handle all shopping bag processes"""
    
    return render(request, 'shopping_bag/shopping_bag.html')

