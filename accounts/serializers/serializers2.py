from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from ..models.models2 import Follow,Project,Skill,SocialMedia,UserSocialMediaAccounts,EducationCategory,UserEducation,WorkExperience

'''
Serializers: 

UserSocialMediaAccounts
Follow
Project
Skill
SocialMedia
EducationCategory
UserEducation
WorkExperience
'''

class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class UserSocialMediaAccountsSerializer(ModelSerializer):
    social_media = SocialMediaSerializer()
    class Meta:
        model = UserSocialMediaAccounts
        fields = '__all__'

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectSerializer(ModelSerializer):
    skills_used = SkillSerializer(many=True)
    class Meta:
        model = SocialMedia
        fields = '__all__'

class ProjectSerializer(ModelSerializer):
    skills_used = SkillSerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'

class EducationCategorySerializer(ModelSerializer):
    class Meta:
        model = EducationCategory
        fields = '__all__'


class UserEducationSerializer(ModelSerializer):
    category = EducationCategory()
    class Meta:
        model = UserEducation
        fields = '__all__'

class WorkExperienceSerializer(ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'