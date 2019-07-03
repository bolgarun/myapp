from channels.generic.websocket import AsyncWebsocketConsumer
import json
from myapp.models import Messages, Chat
import datetime
from messenger.settings import ISO_FORMAT


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['chat_id']
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender_username = text_data_json['username']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': sender_username
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        chat = Chat.objects.get(id=self.room_name)
        message = event['message']
        user = self.scope['user']
        sender_username = event.get("username")
        if sender_username and sender_username == user.username:
            message = Messages(
                chat=chat,
                author=user,
                text=message,
                )
            message.save()

        await self.send(text_data=json.dumps({
            'message': message if isinstance(message, str) else message.text,
            'author': sender_username,
            'created_at': datetime.datetime.now().strftime(ISO_FORMAT)
        }))