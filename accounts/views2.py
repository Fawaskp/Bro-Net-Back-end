from .models.models2 import Follow,Project,Skill,SocialMedia,UserSocialMediaAccounts,EducationCategory,UserEducation,WorkExperience
from .models import UserProfile
from .serializers.serializers2 import SkillSerializer,SocialMediaSerializer,ProjectSerializer,UserSocialMediaAccountsSerializer,\
UserEducationSerializer,WorkExperienceSerializer,EducationCategorySerializer
from .serializers.serializers import UserViewSerializer,UserProfileSerializer
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class SkillView(ListAPIView):
    serializer_class = SkillSerializer

    def get_queryset(self):
        skill_id = self.request.query_params.get('skill_id')

        if skill_id:
            try:
                skill = Skill.objects.get(pk=skill_id)
                queryset = [skill] 
            except Skill.DoesNotExist:
                queryset = Skill.objects.none()
        else:
            queryset = Skill.objects.all()

        return queryset

 
class SkillDetail(APIView):

    def get_user_profile(self, user_id):
        try:
            user_profile = UserProfile.objects.get(user_id=user_id)
            return user_profile
        except UserProfile.DoesNotExist:
            return None

    def put(self, request, id):
        user_profile = self.get_user_profile(id)
        if not user_profile:
            return Response({'Message': 'Data Not Found', 'status': 404})

        existing_skills = list(user_profile.skills.all())
        skill_id = request.data.get('skill_id')

        if not skill_id:
            return Response({'Message': 'Skill ID not provided in the request data', 'status': 400})

        try:
            new_skill = Skill.objects.get(pk=skill_id)
        except Skill.DoesNotExist:
            return Response({'Message': 'Invalid Skill ID', 'status': 400})

        if new_skill in existing_skills:
            return Response({'Message': new_skill.name+' is already in your profile', 'status': 400})
        else:
            existing_skills.append(new_skill)
            user_profile.skills.set(existing_skills)
            user_profile.save()
            return Response({'Message': 'Skill added successfully', 'status': 200})

    def delete(self, request, id):
        user_profile = self.get_user_profile(id)
        if not user_profile:
            return Response({'Message': 'Data Not Found', 'status': 404})

        skill_id = request.data.get('skill_id')

        if not skill_id:
            return Response({'Message': 'Skill ID not provided in the request data', 'status': 400})

        try:
            skill_to_remove = Skill.objects.get(pk=skill_id)
        except Skill.DoesNotExist:
            return Response({'Message': 'Invalid Skill ID', 'status': 400})

        if skill_to_remove in user_profile.skills.all():
            user_profile.skills.remove(skill_to_remove)
            return Response({'Message': 'Skill removed successfully', 'status': 200})
        else:
            return Response({'Message': 'Skill is not present in your profile', 'status': 400})


class UserSocialMediaAccountsView(ListAPIView):
    serializer_class = UserSocialMediaAccountsSerializer
    def get_queryset(self):
        user_id      = self.request.query_params.get('user_id')
        if user_id:
            queryset = UserSocialMediaAccounts.objects.filter(user_id=user_id)
        else:
            queryset = []
        return queryset

class EducationCategoriesView(ListAPIView):
    serializer_class = EducationCategorySerializer
    queryset         = EducationCategory.objects.all()

class UserEducationView(ListCreateAPIView):
    serializer_class = UserEducationSerializer
    def get_queryset(self):
        user_id      = self.request.query_params.get('user_id')
        if user_id:
            queryset = UserEducation.objects.filter(user__id=user_id).order_by('category__id')
        else:
            queryset = []
        return queryset
    
    def create(self, request, *args, **kwargs):
        user_id     = request.data.get('user', None)
        institution = request.data.get('institution', None)
        course      = request.data.get('course', None)
        location    = request.data.get('location', None)
        category_id = request.data.get('category', None)

        if not all([user_id, institution, course, location, category_id]):
            return Response({'error': 'Incomplete data provided.'}, status=400)

        try:
            category = EducationCategory.objects.get(pk=category_id)
        except EducationCategory.DoesNotExist:
            return Response({'error': 'Invalid category ID.'}, status=400)

        user_education = UserEducation.objects.create(
            user_id=user_id,
            institution=institution,
            course=course,
            location=location,
            category=category
        )

        serializer = UserEducationSerializer(user_education)
        return Response(serializer.data, status=201)

class UserEducationDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = UserEducationSerializer
    queryset         = UserEducation.objects.all()
    lookup_field     = 'id'

class WorkExperienceView(ListAPIView):
    serializer_class = WorkExperienceSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = WorkExperience.objects.filter(user_id=user_id)
        else:
            queryset = []
        return queryset
    
class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Project.objects.filter(user__id=user_id)
    
class SocialMediaView(ListAPIView):
    queryset         = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer