from rest_framework import serializers
from accounts.models import UserProfile,User

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'fullname', 'username', 'email', 'role', 'is_verified', 'is_active', 'dob', 'is_profile_completed')

class CombinedUserSerializer(serializers.ModelSerializer):
    user_profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'fullname', 'username', 'email', 'role', 'is_verified', 'is_active', 'dob', 'is_profile_completed', 'user_profile')

    def get_user_profile(self, user):
        try:
            return UserProfileSerializer(user.user_profile).data
        except UserProfile.DoesNotExist:
            return None