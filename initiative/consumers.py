import simplejson as json

from channels.generic.websocket import WebsocketConsumer
from channels.db import database_sync_to_async
from numpy.f2py.crackfortran import endifs

from .models import InitEntry


class InitiativeConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()


    def disconnect(self, close_code):
        pass


    def receive(self, text_data):
        message = json.loads(text_data)

        # Initial Load data
        if message["action"] == "init":
            self.send(text_data=json.dumps(self.get_current_list()))

        # Add an entry to the initiative tracker
        elif message["action"] == "add entry":
            if message["entry"] is None:
                self.send(text_data=json.dumps({"error": "'entry' field is required"}))

            self.send(text_data=json.dumps(self.get_current_list()))

        # Apply a condition to a user
        elif message["action"] == "add condition":
            if message["entry"] is None:
                self.send(text_data=json.dumps({"error": "'entry' field is required"}))

            if message["condition"] is None:
                self.send(text_data=json.dumps({"condition": "'entry' field is required"}))

            self.send(text_data=json.dumps(self.get_current_list()))

        # Unexpected case. Report Error
        else:
            self.send(text_data=json.dumps({"error": "Failed to parse action", "message": message}))


    def get_current_list(self):
        data = {}
        for entry in InitEntry.objects.all().order_by('-initiative'):
            data[str(entry.id)] = entry.as_dict()

        return data
