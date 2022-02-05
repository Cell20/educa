import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # """Accept(self.accept()) or Reject(self.close()5) a connection."""
        self.id = self.scope['url_route']['kwargs']['course_id']  # Every consumer has a scope.
        self.room_group_name = 'chat_%s' % self.id
        # join room group
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        # leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {'type': 'chat_message', 'message': message}
        )
        # send message to to associated channel
        # self.send(text_data=json.dumps({'message': message}))

    def chat_message(self, event):
        """Receive message from the group"""
        # Send message to WebSocket
        self.send(text_data=json.dumps(event))
