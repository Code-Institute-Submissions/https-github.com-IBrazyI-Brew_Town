from django.views.generic import TemplateView
from .models import Post

class PostList(TemplateView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts.html'

class PostDetail(TemplateView):
    model = Post
    template_name = 'post_detail.html'

