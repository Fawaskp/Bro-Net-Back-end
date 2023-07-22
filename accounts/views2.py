from .models.models2 import Follow,Project,Skill,SocialMedia
from .serializers.serializers2 import SkillSerializer,SocialMediaSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

class SkillView(ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
 
class SocialMediaView(ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer