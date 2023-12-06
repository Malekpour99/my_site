from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from blog.models import Post, Comment
from blog.forms import CommentForm
from taggit.models import Tag
from django.db.models import Q
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.


def home_view(request, **kwargs):
    posts = Post.objects.filter(
        published_date__lte=timezone.now(), status=True)
    all_tags = Tag.objects.all()
    if kwargs.get("cat_name"):
        posts = posts.filter(category__name=kwargs["cat_name"])
    if kwargs.get("tag_name"):
        posts = posts.filter(tags__name__in=[kwargs["tag_name"]])
    if kwargs.get("author_username"):
        posts = posts.filter(author__username=kwargs["author_username"])

    posts = Paginator(posts, 4)
    try:
        page_number = request.GET.get('page')
        posts = posts.page(page_number)
    except PageNotAnInteger:
        # if page_number is not an integer then return the first page
        posts = posts.page(1)
    except EmptyPage:
        # if page is empty then return the last page
        posts = posts.page(posts.num_pages)
    context = {'posts': posts, 'tags': all_tags}
    return render(request, "blog/blog-home.html", context)


def single_view(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Your Comment Submitted Successfully!")
        else:
            messages.add_message(request, messages.ERROR, "Your Comment Didn't Submit!")

    posts = Post.objects.filter(
        published_date__lte=timezone.now(), status=True)
    post = get_object_or_404(posts, id=pid)
    if not post.require_login:
        comments = Comment.objects.filter(post=post, approved=True)
        tags = post.tags.all()
        form = CommentForm()
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
                'comments': comments,
                'form': form,
                'tags': tags,
                'next_post': next_post,
                'previous_post': previous_post}
        return render(request, "blog/blog-single.html", context)
    else:
        return HttpResponseRedirect(reverse("accounts:login"))


def search_view(request):
    # print(request.__dict__) # for seeing request contents
    posts = Post.objects.filter(
        published_date__lte=timezone.now(), status=True)
    if request.method == 'GET':
        # python "warlus" option ( := ) assign the value to the variable -> less code
        if search_query := request.GET.get('search'):
            posts = posts.filter(Q(content__contains=search_query) | Q(title__contains=search_query))
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)
