from rest_framework.generics import ListCreateAPIView
from accounts.models import User,Badges
from accounts.models.models2 import Skill,SocialMedia,Project
from ..serializers.userSerializer import CombinedUserSerializer,SkillSerializer,SocialMediaSerializer,BadgeSerializer,\
ProjectSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import re
from rest_framework.response import Response
from django.http import JsonResponse
from accounts.helpers import email_validator,create_jwt_pair_tokens
from django.contrib.auth import authenticate, login, logout

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

@api_view(['POST'])
@csrf_exempt
def admin_login(request):
    if request.method == 'POST':
        email = request.data.get('email')
        password = request.data.get('password')
        if email and password:
            if not email_validator(email):
                return Response(data={"message": "Invalid E-mail format", "status": 400})
            else:
                print(email,' ',password)
                username = authenticate(email=email,password=password)
                if username:
                    try:
                        user = User.objects.get(username=username)
                    except:
                        return JsonResponse(data={"message":"Enter valid data","status":400})
                    if user.is_superuser:
                        token = create_jwt_pair_tokens(user)
                        return JsonResponse(data={'token':token},status=202)
                    else:
                        return JsonResponse(data={"message":"Credential is missing","status":400})
                else:
                    return JsonResponse(data={"message":"Enter valid data","status":400})
        else:
            return JsonResponse(data={"message":"Credential is missing","status":400})
    else:
        return JsonResponse(data={'detail':"is not allowed"},status=405)


