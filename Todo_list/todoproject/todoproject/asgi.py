"""
ASGI config for todoproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from todo.routing import websocket_urlpatterns
from django.core.asgi import get_asgi_application

# Set default settings module for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'todoproject.settings')

# Setup Django
django.setup()

# Define the ASGI application for both HTTP and WebSocket
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
