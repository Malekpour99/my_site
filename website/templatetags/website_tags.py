from django import template
from blog.models import Post
import datetime

register = template.Library()


@register.inclusion_tag('website/includes/latest-from-blog.html')
def latest_posts(num=6):
    "Retrieving latest posts"
    posts = Post.objects.filter(published_date__lte=datetime.datetime.now(),
                                status=1).order_by('-published_date')[:num]
    return {'posts': posts}
