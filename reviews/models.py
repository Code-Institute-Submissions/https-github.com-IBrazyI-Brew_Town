from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=80, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='review_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_on']


    def __str__(self):
        return self.title


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=200, null=True)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['created_on']


    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)