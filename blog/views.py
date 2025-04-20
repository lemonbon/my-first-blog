from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.order_by('-published_date')  # Or .all() if you're just testing
    return render(request, 'blog/post_list.html', {'posts': posts})
