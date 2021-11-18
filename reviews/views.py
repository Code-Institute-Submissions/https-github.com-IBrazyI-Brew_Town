from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Review

def reviews(request):
    reviews = Review.objects.filter(status=1).order_by('-created_on')

    context = {
        'reviews': reviews,
    }

    template = 'reviews/reviews.html'
    return render(request, template, context)


def ReviewsDetails(request, slug):
    review = get_object_or_404(Review, slug=slug)

    context = {
        'review':review
    }

    template = 'reviews/reviews_details.html'
    return render(request, template, context)


