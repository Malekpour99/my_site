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
    current_index = list(posts).index(post)
    previous_post = None
    next_post = None
    if current_index - 1 >= 0:
        next_post = list(posts)[current_index - 1]
    if current_index + 1 < len(list(posts)):
        previous_post = list(posts)[current_index + 1]
    context = {'post': post,
               'next_post': next_post,
               'previous_post': previous_post}
    return render(request, "blog/blog-single.html", context)
