from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from ..models.models2 import Follow,Project,Skill,SocialMedia,UserSocialMediaAccounts

'''
Serializers: 

UserSocialMediaAccounts
Follow
Project
Skill
SocialMedia
'''

class UserSocialMediaAccountsSerializer(ModelSerializer):
    class Meta:
        model = UserSocialMediaAccounts
        fields = '__all__'

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class ProjectSerializer(ModelSerializer):
    skills_used = SkillSerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'