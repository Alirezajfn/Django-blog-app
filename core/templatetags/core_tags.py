from django import template

from blog.models import Post

register = template.Library()


@register.inclusion_tag('core/hero-slider.html')
def popular_posts():
    posts = Post.objects.filter(published=True).order_by('published_at')[:4]
    return {'posts': posts}
