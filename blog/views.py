import datetime
from django.shortcuts import render
from blog.models import Post
# Create your views here.


def home_view(request):
    posts = Post.objects.filter(
        published_date__lte=datetime.datetime.now(), status=True)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)


def single_view(request):
    return render(request, "blog/blog-single.html")
