from django import template

from blog.models import Post, PostImage, Category
from mysite.settings import MEDIA_URL

register = template.Library()


@register.inclusion_tag('core/hero-slider.html')
def popular_posts():
    posts = Post.objects.filter(published=True).order_by('-published_at')[:4]
    for post in posts:
        post.images.set(PostImage.objects.filter(post=post).all())
        print(post.images.first().image.url)
    return {'posts': posts}


@register.inclusion_tag('core/core-categories.html')
def posts_categories():
    categories = Category.objects.filter(top_level=True)[:8]
    if len(categories) < 8:
        categories |= Category.objects.filter(top_level=False)[:8 - len(categories)]
    return {'categories': categories}
