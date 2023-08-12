from django.urls import path
from .views import PostImage,PostVideo,GetAllPost

urlpatterns = [
    path('post-image/',PostImage.as_view()),
    path('post-video/',PostVideo.as_view()),
    path('get-posts/<int:user_id>/',GetAllPost.as_view()),
]