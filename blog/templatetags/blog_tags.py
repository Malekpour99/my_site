from django import template
from blog.models import Post

register = template.Library()


# @register.simple_tag
# def test_tag():
#     pass

# @register.filter
# def test_filter():
#     pass

@register.inclusion_tag('blog/includes/blog-latest-posts.html')
def latest_posts(num=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:num]
    return {'posts': posts}
