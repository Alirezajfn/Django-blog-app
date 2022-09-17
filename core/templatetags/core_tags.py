from django import template

from blog.models import Post, Category


register = template.Library()
posts = Post.objects.filter(published=True)


@register.inclusion_tag('core/hero-slider.html')
def popular_posts():
    p = posts.order_by('-published_at')[:4]
    #p = posts.order_by('-views')[:4]
    return {'posts': p}


@register.inclusion_tag('core/core-categories.html')
def posts_categories():
    categories = Category.objects.filter(top_level=True)[:8]
    if len(categories) < 8:
        categories |= Category.objects.filter(top_level=False)[:8 - len(categories)]
    return {'categories': categories}


@register.inclusion_tag('core/core-footer-recent-posts.html')
def recent_posts():
    p = posts.order_by('-published_at')[:4]
    return {'posts': p}


@register.inclusion_tag('core/core-trending-section.html')
def trending_posts():
    p = posts.order_by('-views')[:5]
    return {'posts': p}


@register.inclusion_tag('core/core-header-categories.html')
def header_categories():
    categories = Category.objects.filter(parent=None)
    return {'categories': categories}