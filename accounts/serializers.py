from rest_framework.serializers import ModelSerializer
from .models import User,UserProfile,Hub,Batch,Stack
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import ValidationError
import re
from .helpers import email_validator

class UserViewSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullname', 'email', 'password', 'is_superuser']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['fullname','username','dob','is_verified']

class LoginSerializer(ModelSerializer):
    
    class Meta:
        model  = User
        fields = ('fullname' , 'email' , 'password')

    def validate(self, attrs):
        email_exist = User.objects.filter(email=attrs['email']).exists()
        if email_exist:
            return ValidationError('This email is already exist')
        return super().validate(attrs)

    def validate_email(self, value):
        email_validator(value)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['profile_image','hub','batch','stack','is_profile_completed']

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

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['email'] = user.email
        token['is_admin'] = user.is_superuser
        
        return token