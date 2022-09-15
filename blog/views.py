from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView

from blog.models import *


def home(request):
    return render(request, 'blog/index.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published=True)


# def posts_list(request):
#     posts = Post.objects.all()
#     context = "\n".join([f"{post.title}, {post.content}" for post in posts])
#     return HttpResponse(context)


def post_detail(request, slug):
    try:
        post = Post.objects.filter(published=True).get(slug=slug)
    except Post.DoesNotExist:
        return HttpResponse('Post not found')
    return HttpResponse(f"Post detail for {post.title}, {post.content}")


class CategoryDetailView(PostListView):
    def get_queryset(self):
        return Post.objects.filter(published=True).filter(categories__category__slug=self.kwargs['slug'])


# def category_detail(request, slug):
#     posts = Post.objects.filter(published=True).filter(categories__category__slug=slug)
#     if not posts:
#         return HttpResponse('Category not found')
#     context = "\n".join([f"{post.title}, {post.content}" for post in posts])
#     return HttpResponse(context)

class TagDetailView(PostListView):
    def get_queryset(self):
        return Post.objects.filter(published=True).filter(tags__tag__slug=self.kwargs['slug'])

# def tag_detail(request, slug):
#     posts = Post.objects.filter(published=True).filter(tags__tag__slug=slug)
#     if not posts:
#         return HttpResponse('Tag not found')
#     context = "\n".join([f"{post.title}, {post.content}" for post in posts])
#     return HttpResponse(context)


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'content', 'author', 'published']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
