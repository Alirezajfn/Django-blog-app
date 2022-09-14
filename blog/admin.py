from django.contrib import admin
from blog.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published', 'created_at', 'updated_at', 'published_at')
    list_filter = ('published', 'created_at', 'updated_at', 'published_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
