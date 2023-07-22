from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import User
from ..serializers.userSerializer import CombinedUserSerializer

class CombinedUserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = CombinedUserSerializer(users, many=True)
        return Response(serializer.data)
