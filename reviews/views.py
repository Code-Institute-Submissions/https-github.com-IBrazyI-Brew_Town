from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm




def reviews(request):

    reviews = Review.objects.order_by('-created_at')
    template = 'reviews/reviews.html'

    return render(request, template, {'reviews':reviews})


@login_required
def add_review(request):
    """Add a review"""
    if not request.user:
        return redirect(reverse('reviews'))
    
    if  request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save()
            messages.success(request, 'Review Added!')
            return redirect(reverse('reviews'))
        else: 
            messages.error(request, 'Review was not added, please try again.')
    else:
        form = ReviewForm()
    template = 'reviews/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)