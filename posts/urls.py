from django.urls import path
from .views import PostImage,PostVideo,GetAllPost,like_post

urlpatterns = [
    path('post-image/',PostImage.as_view()),
    path('post-video/',PostVideo.as_view()),
    path('get-posts/<int:user_id>/',GetAllPost.as_view()),

    path('like-post/<int:id>/',like_post),
]