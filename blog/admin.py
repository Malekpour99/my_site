from django.contrib import admin
from .models import Post, Category
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    # Activates post filtering by date hierarchy
    empty_value_display = '-empty-'
    # Determines how empty values are displayed
    list_display = ('title', 'author', 'counted_views', 'status',
                    'published_date', 'created_date')
    list_filter = ('status', 'author')
    # + "fields" can also be used to determine
    #   which fields to display on each data editing page
    # ordering = ['-created_date'] moved to Meta class
    # Sets the ordering of your data list
    search_fields = ['title', 'content']
    # Determines which fields will be searched for your search query


admin.site.register(Category)
# admin.site.register(Post, PostAdmin)
