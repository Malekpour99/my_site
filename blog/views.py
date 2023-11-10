import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.db.models import Q
# Create your views here.


def home_view(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(
        published_date__lte=datetime.datetime.now(), status=True)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_username:
        posts = posts.filter(author__username=author_username)
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


def search_view(request):
    # print(request.__dict__) # for seeing request contents
    posts = Post.objects.filter(
        published_date__lte=datetime.datetime.now(), status=True)
    if request.method == 'GET':
        # using python "warlus" option ( := ) for less code
        if search_query := request.GET.get('search'):
            posts = posts.filter(Q(content__contains=search_query) | Q(title__contains=search_query))
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)
