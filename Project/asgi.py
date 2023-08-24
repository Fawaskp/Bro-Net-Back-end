"""
ASGI config for Project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Project.settings")
django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from channels.routing import ProtocolTypeRouter, URLRouter
from accounts.routing import websocket_urlpatterns

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": (
            (URLRouter(websocket_urlpatterns))
        ),
    }
)
