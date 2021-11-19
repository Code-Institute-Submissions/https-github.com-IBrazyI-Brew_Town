from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Review
from .forms import CommentForm

def reviews(request):
    reviews = Review.objects.filter(status=1).order_by('-created_on')

    context = {
        'reviews': reviews,
    }

    template = 'reviews/reviews.html'
    return render(request, template, context)


def reviews_details(request, slug):
    template_name = 'reviews/reviews_details.html'
    review = get_object_or_404(Review, slug=slug)
    comments = review.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.review = review
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'review': review,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})
