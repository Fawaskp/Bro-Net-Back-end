from rest_framework.serializers import ModelSerializer
from ..models import User,UserProfile,Hub,Batch,Stack
from .serializers2 import SkillSerializer
'''
Serializers: 

User
UserDetail
UserProfile
Stack
Hub
Batch
'''

class HubSerializer(ModelSerializer):
    class Meta:
        model = Hub
        fields = '__all__'


class BatchSerializer(ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'


class StackSerializer(ModelSerializer):
    class Meta:
        model = Stack
        fields = '__all__'

class UserViewSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullname','username','email', 'password', 'is_profile_completed']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['fullname','email','username','dob','is_verified','is_profile_completed']


class UserProfileSerializer(ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    hub    = HubSerializer(read_only=True)
    batch  = BatchSerializer(read_only=True)
    stack  = StackSerializer(read_only=True)
    class Meta:
        model = UserProfile
        fields = '__all__'
        