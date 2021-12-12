from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """
    Renders the shopping bag page,
     will also handle all shopping bag processes
    """

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """ Add items to the shopping bag, able to add different quantitys """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request,
                         f'Changed {product.name} quantity to {bag[item_id]}.')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to bag.')

    request.session['bag'] = bag
    return redirect(redirect_url)


def edit_bag(request, item_id):
    """ Adjust the ammount of each item within the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request,
                         f'Changed {product.name} quantity to {bag[item_id]}.')
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from bag.')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove an item from the shopping bag """

    product = get_object_or_404(Product, pk=item_id)

    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from bag.')

        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
