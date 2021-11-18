from django.shortcuts import render

def reviews(request):
    template = 'reviews/reviews.html'
    return render(request, template)
