from rest_framework.generics import ListCreateAPIView, ListAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BannerSerializer, PostSerializer,PostCommentsSerializer
from .models import Banner, Post, ImagePost, VideoPost, PollPost, PostComment
from accounts.models import User
from accounts.models.models2 import Follow
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

"""
BannerView
GetAllPost
PostImage
PostVideo
"""
class DefaultPagination(PageNumberPagination):
    page_size = 3

class BannerView(ListCreateAPIView):
    serializer_class = BannerSerializer
    queryset         = Banner.objects.all().order_by('id')
    pagination_class = DefaultPagination

@api_view(['GET'])
def get_active_banner(request):
    active = Banner.objects.filter(status=True).last()
    if active:
        return Response(data=BannerSerializer(active).data)
    else:
        return Response(status=404)

class BannerDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = BannerSerializer
    queryset         = Banner.objects.all()
    lookup_field     = 'id'
    pagination_class = DefaultPagination

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
                return queryset.order_by('-id')
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
        except Exception as e :
            print('This is the Excetion ::>> ',e)
            return Response(status=400, data={"message": "failed"})
        try:
            VideoPost.objects.create(post=post_instance, video=request.FILES.get('video'))
        except Exception as e :
            return Response(status=400, data={"message": f" {e}"})
        return Response(status=200, data={"message": "success"})


class PostPoll(APIView):
    def post(self, request):
        user_id = request.data.get("user")
        optioncount = request.data.get("optionscount")
        subject = request.data.get("subject")
        options = []
        print('Request Data >>>? ',request.data)
        if "" in [user_id,optioncount,subject] and None in [user_id,optioncount,subject]:
            return Response(status=400, data={"message": "Bad request with some empty data field"})

        for count in range(1,int(optioncount)+1):
            if not request.data.get(f'option{count}') == '': 
                options.append(request.data.get(f'option{count}'))
            else:
                return Response(status=400, data={"message": f"Null option found ({count})"})

        try:
            user_instance = User.objects.get(id=user_id)
            post_instance = Post.objects.create(
                user=user_instance, 
                type="poll",
                poll_subject=subject,
            )
        except Exception as e :
            return Response(status=400, data={"message": f"{e}"})
        try:
            for option in options:
                PollPost.objects.create(post=post_instance,option=option)
        except Exception as e :
            return Response(status=400, data={"message": f" {e}"})
        return Response(status=200, data={"message": "success"})


class PostCommentsView(ListCreateAPIView):
    serializer_class = PostCommentsSerializer
    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        return PostComment.objects.filter(post__id=post_id)


@api_view(["PUT", "PATCH"])
def like_post(request, id):
    is_post_exist = Post.objects.filter(id=id)
    if is_post_exist:
        post_instance = Post.objects.get(id=id)
        post_instance.like_count += 1
        post_instance.save()
        return Response(status=200)
    else:
        return Response(status=404, data={"message": "given post not found"})
