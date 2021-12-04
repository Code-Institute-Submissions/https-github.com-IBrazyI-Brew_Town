from .models import Comment, Review
from django.forms import ModelForm
from django import forms


class ReviewForm(forms.ModelForm):
    model = Review
    fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)