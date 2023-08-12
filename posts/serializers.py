from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Banner,Post,ImagePost,VideoPost,ArticlePost
from accounts.serializers.serializers import UserViewSerializer, UserProfileSerializer
from accounts.models import UserProfile

class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class ImagePostSerializer(ModelSerializer):
    class Meta:
        model = ImagePost
        fields = ['post','image']

class VideoPostSerializer(ModelSerializer):
    class Meta:
        model = VideoPost
        fields = '__all__'

class ArticlePostSerializer(ModelSerializer):
    class Meta:
        model = ArticlePost
        fields = '__all__'

class PostSerializer(ModelSerializer):
    post = SerializerMethodField()
    user = SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'
    
    def get_post(self,obj):
        if obj.type == 'image':
            post = []
            instances = ImagePost.objects.filter(post=obj)
            for instance in instances:
                post.append((ImagePostSerializer(instance).data.get('image')))
            return post
        elif obj.type == 'video':
            return [VideoPostSerializer(VideoPost.objects.get(post=obj)).data.get('video')]
    
    def get_user(self,obj):
        result = {}
        result.update(fullname=UserViewSerializer(obj.user).data.get('fullname'))
        result.update(username=UserViewSerializer(obj.user).data.get('username'))
        userprofile_instance = UserProfile.objects.get(user=obj.user)
        result.update(profile_image=UserProfileSerializer(userprofile_instance).data.get('profile_image'))
        return result