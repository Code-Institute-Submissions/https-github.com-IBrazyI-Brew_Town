from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    review_title = models.CharField(max_length=50, null=True)
    review_author = models.ForeignKey(User,
                                      on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_text = models.TextField(max_length=200, null=True)

    def __str__(self):
        return self.review_title


class Comment(models.Model):
    comment_review = models.ForeignKey(Review,
                                       on_delete=models.CASCADE, null=True)
    comment_author = models.ForeignKey(User,
                                       on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment_text = models.TextField(max_length=200, null=True)

    def __str__(self):
        return f'"{self.comment_author.username}"n\
         commented on "{self.comment_review.review_title}"'
