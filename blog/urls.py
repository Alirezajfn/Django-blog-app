from django.urls import path
from blog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.PostListView.as_view(), name='posts_list'),
    path('details/<slug:slug>', views.post_detail, name='post_detail'),
    path('category/<slug:slug>', views.CategoryDetailView.as_view(), name='category_detail'),
    path('tag/<slug:slug>', views.TagDetailView.as_view(), name='tag_detail'),
]
