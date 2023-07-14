from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import UserSerializer, UserProfileSerializer
from .models import User,UserProfile

class ViewUsers(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ViewUserProfile(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
