from django.shortcuts import render, redirect

def view_bag(request):
    """Renders the shopping bag page, will also handle all shopping bag processes"""
    
    return render(request, 'shopping_bag/shopping_bag.html')

def add_to_bag(request, item_id):
    """ Add items to the shopping bag, able to add different quantitys """

    quantity = request.POST.get('quanity')
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)