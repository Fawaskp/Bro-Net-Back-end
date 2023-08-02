from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User,UserProfile,Hub,Batch,Stack
from .serializers.serializers import UserViewSerializer, UserDetailSerializer,UserProfileSerializer,\
HubSerializer,BatchSerializer, StackSerializer
from .permission import IsAuthenticatedWithToken


'''
ViewUsers
UserDetail
ViewUserProfile
UserProfileDetail

GetStackList
GetHubList
GetBatchList
'''

class ViewUsers(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserViewSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'id'

class ViewUserProfile(CreateAPIView):
    queryset = UserProfile.objects.all()

class UserProfileDetail(APIView):
    permission_classes = [IsAuthenticatedWithToken]
    def put(self, request ,id):
        try:
            user_profile = UserProfile.objects.get(user_id=id)
        except:
            return Response({'Message' : 'Data Not Found',"status":status.HTTP_404_NOT_FOUND})
        
        serializer = UserProfileSerializer(user_profile, data=request.data)
        # print('Request Data : ',request.data)
        if serializer.is_valid():
            serializer.save()
            user_profile.is_profile_completed = True
            user_profile.save()
            user = User.objects.get(id=id)
            user.is_profile_completed = True
            user.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message' : serializer.errors,"status":status.HTTP_400_BAD_REQUEST})
        
    def get(self, request, id):
        try:
            user_profile = UserProfile.objects.get(user_id=id)
        except:
            return Response({'Message': 'Data Not Found',"status":status.HTTP_404_NOT_FOUND})
        else:
            serializer = UserProfileSerializer(user_profile)
            return Response(data=serializer.data, status=status.HTTP_200_OK)

class GetStackList(ListAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer

class GetHubList(ListAPIView):
    queryset = Hub.objects.all()
    serializer_class = HubSerializer

class GetBatchList(ListAPIView):
    serializer_class = BatchSerializer
    def get_queryset(self):
        hub_id = self.request.query_params.get('hub_id', '')
        if hub_id and Hub.objects.filter(id=hub_id).exists() :
            hub_instance = Hub.objects.get(id=hub_id)
            return Batch.objects.filter(hub=hub_instance)
        return {}
    

