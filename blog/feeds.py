from django.contrib.syndication.views import Feed
from django.utils import timezone
from django.urls import reverse
from blog.models import Post


class LatestPostsFeed(Feed):
    title = "Blog Latest Posts"
    link = "/rss/feed"
    description = "Updates on the latest blog posts"

    def items(self):
        return Post.objects.filter(published_date__lte=timezone.now(), status=True)[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:100]

    # item_link is only needed if NewsItem has no get_absolute_url method.
    # def item_link(self, item):
    #     return reverse("blog:single", args={"pid": item.id})