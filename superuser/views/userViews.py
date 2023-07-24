from rest_framework.generics import ListCreateAPIView
from accounts.models import User,Badges
from accounts.models.models2 import Skill,SocialMedia,Project
from ..serializers.userSerializer import CombinedUserSerializer,SkillSerializer,SocialMediaSerializer,BadgeSerializer,\
ProjectSerializer

# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.authentication import TokenAuthentication

class StudetsView(ListCreateAPIView):
    queryset = User.objects.filter(role='student')
    serializer_class = CombinedUserSerializer

class CouncellorsView(ListCreateAPIView):
    queryset = User.objects.filter(role='academic_counselor')
    serializer_class = CombinedUserSerializer

class AdminsView(ListCreateAPIView):
    queryset = User.objects.filter(role='brototype_admin')
    serializer_class = CombinedUserSerializer

class CoOrdinatorsView(ListCreateAPIView):
    queryset = User.objects.filter(role='review_coordinator')
    serializer_class = CombinedUserSerializer

class SkillsView(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class SocialMediaView(ListCreateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class BadgesView(ListCreateAPIView):
    queryset = Badges.objects.all()
    serializer_class = BadgeSerializer

class ProjectView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

