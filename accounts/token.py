from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

User = get_user_model()


def create_jwt_pair_tokens(user: User):
    refresh = RefreshToken.for_user(user)

    # Custom user details to be added to the tokens
    custom_data = {
        "user_id": user.id,
        "fullname": user.fullname,
        "email": user.email,
    }

    # Update the token's payload with custom data
    refresh['custom'] = custom_data

    tokens = {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }

    return tokens