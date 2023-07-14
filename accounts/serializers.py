from rest_framework.serializers import ModelSerializer
from .models import User,UserProfile

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullname', 'email', 'password', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'