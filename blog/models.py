from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=75)
    meta_title = models.CharField(max_length=100, null=True, blank=True)  # The meta title to be used for browser title.
    slug = models.SlugField(max_length=100, unique=True)
    summary = models.TextField(max_length=500, null=True)
    published = models.BooleanField(default=False)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title


class PostMeta(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='meta')
    key = models.CharField(max_length=50)
    value = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.key


class Comment(models.Model):
    title = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    content = models.TextField(null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title


class BaseCategoryTag(models.Model):
    title = models.CharField(max_length=75)
    meta_title = models.CharField(max_length=100, null=True, blank=True)  # The meta title to be used for browser title.
    slug = models.SlugField(max_length=100, unique=True)
    content = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title


class Category(BaseCategoryTag):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.category.title


class Tag(BaseCategoryTag):
    class Meta:
        verbose_name = 'Tag'


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.tag.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images')
    caption = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.image.name


class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title + ' - ' + self.user.username
