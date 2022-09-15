from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts_list, name='posts_list'),
    path('details/<slug:slug>', views.post_detail, name='post_detail'),
    path('category/<slug:slug>', views.category_detail, name='category_detail'),
    path('tag/<slug:slug>', views.tag_detail, name='tag_detail'),
]
