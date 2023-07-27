from django.shortcuts import render
from .models import Post

# Create your views here.
def community(request):
    posts = Post.objects.all().order_by('-pk')
    post = {
        'posts':posts
    }

    return render(request, 'blog/community.html', post)