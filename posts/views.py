from rest_framework.generics import ListCreateAPIView,ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BannerSerializer, PostSerializer
from .models import Banner, Post, ImagePost, VideoPost
from accounts.models import User
from accounts.models.models2 import Follow
from rest_framework.decorators import api_view

"""
BannerView
GetAllPost
PostImage
PostVideo
"""


class BannerView(ListCreateAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()


class GetAllPost(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        queryset = Post.objects.none()
        try:
            if user_id is not None:
                user = User.objects.get(id=user_id)
                followings = Follow.objects.filter(following_user=user)
                for instance in followings:
                    queryset = queryset | Post.objects.filter(
                        user=instance.followed_user
                    )
                return queryset
        except:
            return []


class PostImage(APIView):
    def post(self, request):
        user_id = request.data.get("user")
        description = request.data.get("description")
        try:
            user_instance = User.objects.get(id=user_id)
            post_instance = Post.objects.create(
                user=user_instance, type="image", description=description
            )
        except:
            return Response(status=400, data={"message": "failed"})

        try:
            for i in range(len(request.FILES)):
                ImagePost.objects.create(
                    post=post_instance, image=request.FILES.get(f"image[{str(i)}]")
                )
        except:
            return Response(status=400, data={"message": "something went wrong"})

        return Response(status=200, data={"message": "sucess"})


class PostVideo(APIView):
    def post(self, request):
        user_id = request.data.get("user")
        description = request.data.get("description")
        try:
            user_instance = User.objects.get(id=user_id)
            post_instance = Post.objects.create(
                user=user_instance, type="video", description=description
            )
        except:
            return Response(status=400, data={"message": "failed"})

            VideoPost.objects.create(post=post_instance, video=request.FILES)
            return Response(status=400, data={"message": f"{e}"})

        return Response(status=200, data={"message": "sucess"})

@api_view(['PUT','PATCH'])
def like_post(request,id):
    is_post_exist = Post.objects.filter(id=id)
    if is_post_exist:
        post_instance = Post.objects.get(id=id)
        post_instance.like_count += 1
        post_instance.save()
        return Response(status=200)
    else:
        return Response(status=404,data={'message':'given post not found'})
