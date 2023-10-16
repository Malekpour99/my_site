from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    # image
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag
    # category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField()
    published_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
        # ordering applied here is general, not just limited to the admin page
        # you can change your presented class name
        #   using "verbose_name" and "verbose_name_plural"

    def __str__(self):
        return f" {self.title} - {self.id}"
