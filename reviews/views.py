from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review, Comment
from .forms import CommentForm



def reviews(request):
    reviews = Review.objects.order_by('-created_on')

    template = 'reviews/reviews.html'
    return render(request, template, {'reviews':reviews})


@login_required
def delete_review(request, slug):
    """ Delete a review, only if superuser or the review creator """
    if not request.user.is_superuser:
        return redirect('reviews.html')
    review = get_object_or_404(Review, slug=slug)
    review.delete()
    messages.success(request, 'Review Deleted!')
    return redirect(reverse('reviews'))
     

def reviews_details(request, slug):
    template_name = 'reviews/reviews_details.html'
    review = get_object_or_404(Review, slug=slug)
    comments = Comment.objects.order_by(('-created_on'))
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object
            new_comment = comment_form.save
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
