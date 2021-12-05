from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review




def reviews(request):
    reviews = Review.objects.order_by('-created_at')

    template = 'reviews/reviews.html'
    return render(request, template, {'reviews':reviews})
