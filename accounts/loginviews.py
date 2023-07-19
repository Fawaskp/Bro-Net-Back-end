from rest_framework.validators import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User,LoginWithEmailData
from .token import create_jwt_pair_tokens
from .helpers import email_validator,generate_token,email_sender

class LoginWithEmail(APIView):

    def get(self, request):
        token = request.GET.get('token')

        if not token:
            return Response(data={"message":"token didn't get with request","status":status.HTTP_403_FORBIDDEN})
        try:
            login_instance = LoginWithEmailData.objects.get(token=token)
        except LoginWithEmailData.DoesNotExist:
            return Response(data={'message': 'Enter Valid Link','status':status.HTTP_400_BAD_REQUEST})
        
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
            login_instance.delete()
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

class LoginWithSocialMedia(APIView): 

    def post(self,request):
        email = request.data.get('email')
        try:
            email_validator(email) 
        except ValidationError:
            return Response(data={'message':f'There is an issue with provided E-mail'})

        email_exist = User.objects.filter(email=email).exists()

        if not email_exist:
            username = email.split('@')[0]
            user = User.objects.create_user(email=email,password=email,username=username)
        else:
            user = User.objects.get(email=email)
            
        return Response(data={'Token': create_jwt_pair_tokens(user),'status':200}, status=status.HTTP_200_OK)
