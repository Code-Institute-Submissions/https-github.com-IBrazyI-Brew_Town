from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


def view_all_products(request):
    """ Renders the products page, displays the products model and
    handles all sorting and searching queries
    """

    products = Product.objects.all()
    query = ""
    categories = ""

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter an item youn\
                 would like to search.")
                return redirect(reverse('products'))

        queries = Q(name__icontains=query) | Q(description__icontains=query)
        products = products.filter(queries)

    products_all = {
        'products': products,
        'search_term': query,
        'current_categories': categories
        }

    return render(request, 'products/products.html', products_all)


def product_details(request, product_id):
    """ Renders the product detail page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def product_management(request):
    """
    Renders the product management page,
    where the store owners will be able to select from,
    add edit and removal of products
    """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = SelectProductForm(request.POST, request.FILES)

    template = 'products/product_management.html'

    return render(request, template)


@login_required
def add_product(request):
    "Add a product to the store without using the admin page"
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Product failed to add,n\
             please check the information is valid')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product from the store """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.n\
             Please try again.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete product from the store """
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
