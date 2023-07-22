from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from ..models.models2 import Follow,Project,Skill,SocialMedia

'''
Serializers: 

Follow
Project
Skill
SocialMedia
'''

class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class SocialMediaSerializer(ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'