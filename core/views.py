from django.shortcuts import render, get_object_or_404
from blog.models import Post, Category


def home(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def contact(request):
    return render(request, 'core/contact.html')
