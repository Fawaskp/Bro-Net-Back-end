from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BannerSerializer
from .models import Banner, Post, ImagePost
from accounts.models import User
from .serializers import ImagePostSerializer
from accounts.serializers.serializers import UserViewSerializer
from accounts.models import UserProfile

class BannerView(ListCreateAPIView):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()


class PostImage(APIView):
    def post(self, request):
        user_id = request.data.get("user")
        post_type = request.data.get("post-type")
        description = request.data.get("description")
        try:
            user_instance = User.objects.get(id=user_id)
            post_instance = Post.objects.create(
                user=user_instance, type=post_type, description=description
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


class GetPosts(ListCreateAPIView):
    queryset = ImagePost.objects.all()
    serializer_class = ImagePostSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        posts_dict = {} 

        for post in queryset:
            post_id = post.post.id
            if post_id not in posts_dict:
                posts_dict[post_id] = {
                    "post": post_id,
                    "images": [],
                    "description":post.post.description,
                    "user": {
                        'fullname' : UserViewSerializer(post.post.user).data.get('fullname'),
                        'profile_img' : UserProfile.objects.get(user=post.post.user).profile_image.url,
                        'id' : UserViewSerializer(post.post.user).data.get('id'),
                    }
                }

            posts_dict[post_id]["images"].append(post.image.url)

        posts_list = list(posts_dict.values())
        return Response(posts_list, status=200)
