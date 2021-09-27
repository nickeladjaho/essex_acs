from django.urls import path

from .views import PostListView, PostDetailView

urlpatterns = [
    path('posts/<slug:slug>', PostDetailView.as_view(), name='post_detail'),
    path('posts', PostListView.as_view(), name='post_list'),
]
