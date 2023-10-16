import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import Post
# Create your views here.


def home_view(request):
    posts = Post.objects.filter(
        published_date__lte=datetime.datetime.now(), status=True)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)


def single_view(request, pid):
    posts = Post.objects.filter(
        published_date__lte=datetime.datetime.now(), status=True)
    post = get_object_or_404(posts, id=pid)
    # post = get_object_or_404(Post, id=pid) # this is unsafe because you can access not published posts by using ID
    post.counted_views += 1
    post.save()
    context = {'post': post}
    return render(request, "blog/blog-single.html", context)
