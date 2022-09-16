from django.contrib import admin
from django.contrib.admin import register

from blog.models import *


class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1


@register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published', 'created_at', 'updated_at', 'published_at')
    list_filter = ('published', 'created_at', 'updated_at', 'published_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    inlines = [PostCategoryInline]


@register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('post', 'category')
    list_filter = ('post', 'category')
    search_fields = ('post', 'category')


admin.site.register(Category, inline=PostCategoryInline)
admin.site.register(Tag)
admin.site.register(PostTag)
admin.site.register(Comment)
admin.site.register(PostMeta)
admin.site.register(PostImage)
