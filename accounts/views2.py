from .models.models2 import Follow,Project,Skill,SocialMedia,UserSocialMediaAccounts,EducationCategory,UserEducation,WorkExperience
from .models import UserProfile
from .serializers.serializers2 import SkillSerializer,SocialMediaSerializer,ProjectSerializer,UserSocialMediaAccountsSerializer,UserEducationSerializer,WorkExperienceSerializer
from .serializers.serializers import UserViewSerializer,UserProfileSerializer
from rest_framework.generics import ListAPIView,ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class SkillView(ListAPIView):
    serializer_class = SkillSerializer

    def get_queryset(self):
        skill_id = self.request.query_params.get('skill_id')

        if skill_id:
            try:
                skill = Skill.objects.get(pk=skill_id)
                queryset = [skill]  # Convert the single skill to a list
            except Skill.DoesNotExist:
                queryset = Skill.objects.none()
        else:
            queryset = Skill.objects.all()

        return queryset

 
class AddSkill(APIView):
    def put(self, request, id):
        try:
            user_profile = UserProfile.objects.get(user_id=id)
        except UserProfile.DoesNotExist:
            return Response({'Message': 'Data Not Found', "status": 404})

        existing_skills = list(user_profile.skills.all())
        skill_id = request.data.get('skill_id')

        if not skill_id:
            return Response({'Message': 'Skill ID not provided in the request data', "status": 400})
        
        try:
            new_skill = Skill.objects.get(pk=skill_id)
        except Skill.DoesNotExist:
            return Response({'Message': 'Invalid Skill ID', "status": 400})

        if new_skill in existing_skills:
            return Response({'Message': new_skill.name+' is already in your profile', "status": 400})
        else:
            existing_skills.append(new_skill)
            user_profile.skills.set(existing_skills)
            user_profile.save()
            return Response({'Message': 'Skill added successfully','status':200})


class UserSocialMediaAccountsView(ListAPIView):
    serializer_class = UserSocialMediaAccountsSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = UserSocialMediaAccounts.objects.filter(user_id=user_id)
        else:
            queryset = []
        return queryset

class UserEducationView(ListAPIView):
    serializer_class = UserEducationSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = UserEducation.objects.filter(user__id=user_id)
        else:
            queryset = []
        return queryset

class WorkExperienceView(ListAPIView):
    serializer_class = WorkExperienceSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = WorkExperience.objects.filter(user_id=user_id)
        else:
            queryset = []
        return queryset
    
class ProjectView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = Project.objects.filter(user_id=user_id)
        else:
            queryset = Project.objects.all()
        return queryset
    
class SocialMediaView(ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer