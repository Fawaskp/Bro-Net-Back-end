from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.validators import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User,UserProfile,LoginWithEmailData,Hub,Batch,Stack
from .token import create_jwt_pair_tokens
from .helpers import email_validator,generate_token,email_sender
from .serializers import UserViewSerializer, UserDetailSerializer,UserProfileSerializer, \
MyTokenObtainPairSerializer,LoginSerializer, HubSerializer,BatchSerializer, StackSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class ViewUsers(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserViewSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'id'

class ViewUserProfile(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = LoginSerializer

class UserProfileDetail(APIView):
    def put(self, request ,id):
        try:
            user_profile = UserProfile.objects.get(user_id=id)
        except:
            return Response({'Message' : 'Data Not Found',"status":status.HTTP_404_NOT_FOUND})
        
        serializer = UserProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            user_profile.is_profile_completed = True
            user_profile.save()
            return Response({'Message' : 'User Profile Successfully Updated'}, status=status.HTTP_200_OK)
        else:
            return Response({'Message' : serializer.errors,"status":status.HTTP_400_BAD_REQUEST})
    def get(self, request, id):
        try:
            user_profile = UserProfile.objects.get(user_id=id)
        except UserProfile.DoesNotExist:
            return Response({'Message': 'Data Not Found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = UserProfileSerializer(user_profile)
            return Response(data=serializer.data, status=status.HTTP_200_OK)


class LoginWithEmail(APIView):

    def get(self, request):
        token = request.GET.get('token')

        if not token:
            return Response(data={"message":"token didn't get with request","status":status.HTTP_403_FORBIDDEN})
        try:
            login_instance = LoginWithEmailData.objects.get(token=token)
        except LoginWithEmailData.DoesNotExist:
            return Response(data={'message': 'Token not found','status':404})
        
        email = login_instance.email
        elapsed_minutes = login_instance.get_time_elapsed()
        if elapsed_minutes <= 5:
            email_exist = User.objects.filter(email=email).exists()
            
            if not email_exist:
                username = email.split('@')[0]
                user = User.objects.create_user(email=email,password=email,username=username)
            else:
                user = User.objects.get(email=email)
            login_instance.delete()
            return Response(data={'Token': create_jwt_pair_tokens(user),'status':200}, status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Your Link is expired','status':400})
    

    def post(self,request):
        email = request.data.get('email')
        try:
            email_validator(email) 
        except ValidationError:
            return Response(data={'message':f'Enter Valid Email'})
        token = generate_token()       
        link = f'http://localhost:5173/auth/login/?token={token}'
        result = email_sender(email,link)
        if result:
            LoginWithEmailData.objects.create(token=token,email=email)
            return Response(data={'token':token},status=status.HTTP_200_OK)
        else:
            return Response(data={'message':"Email couldn't send","status":status.HTTP_503_SERVICE_UNAVAILABLE})


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
    

