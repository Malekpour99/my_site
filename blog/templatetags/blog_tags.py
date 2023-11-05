from django import template
from blog.models import Post, Category

register = template.Library()


# @register.simple_tag
# def test_tag():
#     pass

# @register.filter
# def test_filter():
#     pass

@register.inclusion_tag('blog/includes/blog-latest-posts.html')
def latest_posts(num=3):
    "Retrieving latest posts"
    posts = Post.objects.filter(status=1).order_by('-published_date')[:num]
    return {'posts': posts}


@register.inclusion_tag('blog/includes/blog-categories.html')
def post_categories():
    "Retrieving categories and counting how many posts are related to them"
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for category in categories:
        cat_dict[category] = posts.filter(category=category).count()
    return {'categories': cat_dict}
