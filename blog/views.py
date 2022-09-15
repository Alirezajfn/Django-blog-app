from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from blog.models import *


def home(request):
    return HttpResponse('Hello, World!')


def posts_list(request):
    posts = Post.objects.all()
    context = "\n".join([f"{post.title}, {post.content}" for post in posts])
    return HttpResponse(context)


def post_detail(request, slug):
    try:
        post = Post.objects.filter(published=True).get(slug=slug)
    except Post.DoesNotExist:
        return HttpResponse('Post not found')
    return HttpResponse(f"Post detail for {post.title}, {post.content}")


def category_detail(request, slug):
    posts = Post.objects.filter(published=True).filter(categories__category__slug=slug)
    if not posts:
        return HttpResponse('Category not found')
    context = "\n".join([f"{post.title}, {post.content}" for post in posts])
    return HttpResponse(context)


def tag_detail(request, slug):
    posts = Post.objects.filter(published=True).filter(tags__tag__slug=slug)
    if not posts:
        return HttpResponse('Tag not found')
    context = "\n".join([f"{post.title}, {post.content}" for post in posts])
    return HttpResponse(context)