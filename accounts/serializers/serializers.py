from rest_framework.serializers import ModelSerializer
from ..models import User,UserProfile,Hub,Batch,Stack

'''
Serializers: 

User
UserDetail
UserProfile
Stack
Hub
Batch
'''

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
        fields = ['fullname','username','dob','is_verified','is_profile_completed']


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['profile_image','hub','batch','stack']

class StackSerializer(ModelSerializer):
    class Meta:
        model = Stack
        fields = '__all__'
        
class HubSerializer(ModelSerializer):
    class Meta:
        model = Hub
        fields = '__all__'


class BatchSerializer(ModelSerializer):
    class Meta:
        model = Batch
        fields = '__all__'