from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()


def create_jwt_pair_tokens(user: User):
    refresh = RefreshToken.for_user(user)

    custom_data = {
        "user_id": user.id,
        "fullname": user.fullname,
        "username": user.username,
        "email": user.email,
        "is_profile_completed": user.is_profile_completed,
    }

    refresh['custom'] = custom_data

    tokens = {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }

    return tokens