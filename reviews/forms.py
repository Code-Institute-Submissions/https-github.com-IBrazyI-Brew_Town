from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_title', 'review_text']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text', ]
