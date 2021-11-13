from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.context import bag_contents

import stripe

def checkout(request):
    """  Checks if the is a user bag, creates order form and renders the template for the checkout page """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty.")
        return redirect(reverse('products'))
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JvI9LCvO1HFcJuqLIh1e86ReRsh578qtLAC1VnCIoEKs7fov6fBA3UfkWeL9P7u6ZxFkORn7V82qQoJBh6mM92p008fnSG9NE',
        'client_secret': 'test_client_secret'
    }

    return render(request, template, context)