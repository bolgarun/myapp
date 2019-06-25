from django.urls import path
from user.consumers import ChatConsumer


websocket_urlpatterns = [
    path('chat-profile-view/<int:chat_id>/', ChatConsumer)
]