import re
from rest_framework.validators import ValidationError
import random
import string
from django.core.mail import send_mail
from django.conf import settings

def generate_token(token_length=20):
    characters = string.ascii_letters + string.digits 
    token = ''.join(random.choice(characters) for _ in range(token_length))
    return token

def email_validator(value:str) -> str:
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    if not re.match(pat,value):
        raise ValidationError("This is not a valid email, try again!")
    return value


def email_sender(email: str, link: str) -> bool:
    try:
        html_message = f'''
        <html>
            <head>
                <style>                    
                    .container {{
                        background-color: white;
                        color:#242424;
                        padding: 20px;
                        border-radius: 5px;
                        display: inline-block;
                        text-align: left;
                    }}
                    
                    .link-button {{
                        display: inline-block;
                        background-color: #6366F1;
                        color: #ffffff!important;
                        text-decoration: none;
                        padding: 10px 20px;
                        border-radius: 3px;
                    }}
                    
                    a {{
                        text-decoration: none;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Hi from Bronet</h1>
                    <p>Follow this link to sign in to Bronet:</p>
                    <a class="link-button" href="{link}">Sign In</a>
                </div>
            </body>
        </html>
        '''

        send_mail(
            "Hi from Bronet",
            '',
            settings.EMAIL_HOST_USER,
            [email],
            html_message=html_message,
            fail_silently=False,
        )
    except:
        return False
    else:
        return True
