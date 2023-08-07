from rest_framework.serializers import ModelSerializer,SerializerMethodField
from ..models import User,UserProfile,Hub,Batch,Stack,Dos,Donts
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
        
class UserSearchSerializer(ModelSerializer):
    profile = SerializerMethodField()
    class Meta:
        model = User
        fields = ('fullname', 'username','email','profile')

    def get_profile(self, user):
        try:
            profile_instance = UserProfile.objects.get(user=user)
            profile_data = {}
            profile_data.update(batch = UserProfileSerializer(profile_instance).data.get('batch').get('batch_name'))
            profile_data.update(image = UserProfileSerializer(profile_instance).data.get('profile_image'))
            return profile_data
        except UserProfile.DoesNotExist:
            return None
        except :
            return None

class DosSerializer(ModelSerializer):
    class Meta:
        model = Dos
        fields = '__all__'

class DontsSerializer(ModelSerializer):
    class Meta:
        model = Donts
        fields = '__all__'