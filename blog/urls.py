from django.urls import path
from .views import BlogPostView,BlogDetailView,BlogCreateView, BlogUpdateView
urlpatterns = [
    path('',BlogPostView.as_view(),name='home'),
    path('post/<int:pk>/',BlogDetailView.as_view(), name='post_detail'),
    path('post/new/',BlogCreateView.as_view(), name = 'post_new'),
    path('post/update/<int:pk>/', BlogUpdateView.as_view(), name='post_update'),
]