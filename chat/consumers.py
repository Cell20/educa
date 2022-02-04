import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        """Accept(self.accept()) or Reject(self.close()5) a connection."""
        self.accept()

    def disconnect(self, close_code):
        """We use pass cuz don't wanna implement any action when client closes the connection."""
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        self.send(text_data=json.dumps({'message': message}))
