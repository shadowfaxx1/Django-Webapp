
from . import views
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeletelView,
                    UserPostListView
                    )
from django.urls import path


urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeletelView.as_view(), name='post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-post'),
    
    path('about/', views.about, name='blog-about'),
]

