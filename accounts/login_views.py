from rest_framework.validators import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import User,LoginWithEmailData
from .helpers import email_validator,generate_token,email_sender,create_jwt_pair_tokens
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .helpers import authenticate_user
import re

'''
check-username
token
is_user_auth
is_user_auth
LoginWithEmail
LoginWithSocialMedia
'''

@api_view(['POST'])
@csrf_exempt
def check_username(request):
    if request.method == 'POST':
        username = request.data.get('username')
        if username:
            regex_pattern = r'^[a-zA-Z0-9_.-]+$'
            if not re.match(regex_pattern, username):
                return Response(data={"message": "Invalid username format", "status": 400})
            is_exist = User.objects.filter(username=username).exists()
            if is_exist:
                return JsonResponse(data={"message":"given username already exist","status":409})
            else:
                return JsonResponse(data={'message':'username is acceptable'},status=202)
        else:
            return JsonResponse(data={"message":"username is important","status":400})
    else:
        return JsonResponse(data={'detail':"is not allowed"},status=405)

@api_view(['POST'])
@csrf_exempt
def token(request):
    if request.method == 'POST':
        email = request.data.get('email')
        if email:
            try:
                userInstance = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response(data={"message": "Something went wrong", "status": 404})
            else:
                token = create_jwt_pair_tokens(userInstance)
                return Response(data={'token': token}, status=202)
        else:
            return Response(data={"message": f"email is important", "status": 400})
    else:
        return Response(data={'detail': f"{request.method} is not allowed"}, status=405)


@api_view(['POST'])
@csrf_exempt
def is_user_auth(request):
    isVerified = authenticate_user(request,'user')
    return JsonResponse(isVerified is not None,safe=False)

@api_view(['POST'])
@csrf_exempt
def is_su_auth(request):
    isVerified = authenticate_user(request,'super_user')
    print('su verification',isVerified)
    return JsonResponse(isVerified is not None,safe=False)


class LoginWithEmail(APIView):

    def get(self, request):
        token = request.GET.get('token')

        if not token:
            return Response(data={"message":"token didn't get with request","status":400})
        try:
            login_instance = LoginWithEmailData.objects.get(token=token)
        except LoginWithEmailData.DoesNotExist:
            return Response(data={'message': 'Enter Valid Link','status':400})
        
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
            return Response(data={'Token': create_jwt_pair_tokens(user),'is_profile_completed':user.is_profile_completed,'status':200})
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
            return Response(data={'token':token,"status":status.HTTP_200_OK})
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

        return Response(data={'Token': create_jwt_pair_tokens(user),'is_profile_completed':user.is_profile_completed,'status':200})