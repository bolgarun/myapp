from channels.generic.websocket import AsyncWebsocketConsumer
import json
from myapp.models import Messages, Chat


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['chat_id']
        self.room_group_name = 'chat_%s' % self.room_name
        # Join room group

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()


    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        print(event['message'])
        chat = Chat.objects.get(id=self.room_name)
        message = event['message']
        message = Messages(
            chat=chat,
            author=self.scope['user'],
            text=message,
            )
        message.save()

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message.text
        }))