import re
from rest_framework.validators import ValidationError
import random
import string
from django.core.mail import send_mail
from django.conf import settings

def generate_token(token_length=20):
    characters = string.ascii_letters + string.digits  # Generate token using letters and digits
    token = ''.join(random.choice(characters) for _ in range(token_length))
    return token

def email_validator(value:str) -> str:
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if not re.match(pat,value):
        raise ValidationError("This is not a valid email, try again!")
    return value

def email_sender(email:str,link:str) -> bool:
    try:
        send_mail( "Hi from Bronet",
        f'Follow this link to sign in to bronet {link}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        )
    except: return False
    else: return True