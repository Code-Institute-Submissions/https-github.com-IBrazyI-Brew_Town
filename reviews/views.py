from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review, Comment
from .forms import ReviewForm, CommentForm




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
            review = form.save(commit=False)
            review.review_author = request.user
            review.save()
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


@login_required
def delete_review(request, review_id):
    """ Delete a review, either a superuser or the creator of the review """
    review = get_object_or_404(Review, pk=review_id)
    current_user = request.user
    review_user = review.review_author
    if current_user == review_user or request.user.is_superuser:
        review.delete()
        messages.success(request, 'Review deleted!')
    else:
        messages.error(request, 'You cannot delete this review.')
        return redirect(reverse('reviews'))

    return redirect(reverse('reviews'))

@login_required
def edit_review(request, review_id):
    """ Edit a review,  either a superuser or the creator of the review """
    review = get_object_or_404(Review, pk=review_id)
    current_user = request.user
    review_user = review.review_author
    if current_user == review_user or request.user.is_superuser:
        if request.method == 'POST':
            form = ReviewForm(request.POST, request.FILES, instance=review) 
            if form.is_valid():
                form.save()
                messages.success(request, 'Review updated')
                return redirect(reverse('reviews'))
            else:
                messages.error(request, 'Failed to update the review. Please try again')
        else:
            form = ReviewForm(instance=review)
            messages.info(request, f'You are editing {review.review_title}')  

        template = 'reviews/edit_review.html'
        context = {
        'form': form,
        'review': review,
        }
    else:
        messages.error(request, 'You cannot edit this review.')
        return redirect(reverse('reviews'))


    return render(request, template, context)

def review_details(request, review_id):
    """ Renders the selected review and its comments """
    review = get_object_or_404(Review, pk=review_id)
    review_name = review.review_title
    review_comments = Comment.objects.all().filter(comment_review=review_id)
    
    template = 'reviews/reviews_details.html'
    context = {
        'review': review,
        'review_title': review_name,
        'review_comments': review_comments,
        'review_id': review_id,
    }

    return render(request, template, context)

@login_required
def add_comment(request, review_id):
    """ Add a comment to selected review """
    review_id = review_id
    review = get_object_or_404(Review, pk=review_id)
    if not request.user:
        return redirect(reverse('reviews'))

    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_review = review
            comment.comment_author = request.user
            comment.save()
            messages.success(request, 'Comment added!')
            return redirect('reviews')
        else: 
            messages.error(request, 'Comment was not added, please try again.')
    else:
        form = CommentForm()
        template = 'reviews/add_comment.html'
        context = {
            'form': form,
            'review_id': review_id,
    }

    return render(request, template, context)

@login_required
def delete_comment(request, comments_id):
    """ Delete a comment, either a superuser or the creator of the comment """
    comment = get_object_or_404(Comment, pk=comments_id)
    current_user = request.user
    review_user = comment.comment_author
    if current_user == review_user or request.user.is_superuser:
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'You cannot delete this comment.')
        return redirect(reverse('reviews'))

    return redirect(reverse('reviews'))
