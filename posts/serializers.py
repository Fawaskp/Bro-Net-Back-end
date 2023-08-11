from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Banner,Post,ImagePost,VideoPost,ArticlePost
from accounts.serializers.serializers import UserViewSerializer

class BannerSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
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