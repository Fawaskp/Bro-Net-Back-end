from django.urls import path
from .views import PostImage,GetPosts

urlpatterns = [
    path('post-image/',PostImage.as_view()),
    path('get-posts/',GetPosts.as_view()),
]
