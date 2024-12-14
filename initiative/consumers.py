import simplejson as json

from channels.generic.websocket import WebsocketConsumer
from .models import InitEntry, Conditions, ConditionOption
from .views import elastic_search_add


def get_current_list():
    data = {}

    # TODO: Update Entry by condition modifiers before sending them back down
    for conditions in Conditions.objects.all():
        pass

    for entry in InitEntry.objects.all().order_by('-initiative'):
        data[str(entry.id)] = entry.as_dict()

    return data


class InitiativeConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()


    def disconnect(self, close_code):
        pass


    def receive(self, text_data):
        message = json.loads(text_data)

        # ----------------
        # Initial Load data
        # ----------------
        if message["action"] == "init":
            self.send(text_data=json.dumps(get_current_list()))


        # ----------------
        # Add an entry to the initiative tracker
        # ----------------
        elif message["action"] == "add":
            # Error Checking
            if message["entry"] is None:
                self.send(text_data=json.dumps({"error": 'Empty Field', "message": "'entry' field is required"}))

            # TODO: Manual Population of an Initiative Entry
            self.send(text_data=json.dumps({"error": 'Unsupported', "message": "This action is not supported. Please develop it!"}))


        # ----------------
        # Add an entry by searching Archives of Nethys
        # ----------------
        elif message["action"] == "search":
            # Error Checking
            if message["query"] is None:
                self.send(text_data=json.dumps({"error": 'Empty Field', "message": "'query' field is required"}))

            # Search for result by name
            result = elastic_search_add(message["query"])

            # Error Handling will always return a string, so forward it on
            if isinstance(result, str):
                self.send(text_data=json.dumps({"error": result, "message": result}))
            else:
                # Add resulting creature to DB and repopulate
                result.save()
                self.send(text_data=json.dumps(get_current_list()))


        # ----------------
        # Apply a condition to an entry
        # ----------------
        elif message["action"] == "affect":
            if message["id"] is None:
                self.send(text_data=json.dumps({"error": 'Empty Field', "message": "'id' field is required"}))
            if message["condition"] is None:
                self.send(text_data=json.dumps({"error": 'Empty Field', "message": "'condition' field is required"}))

            # Manually populate creature and repopulate
            # TODO: Manual Population
            self.send(text_data=json.dumps(get_current_list()))


        # ----------------
        # Remove an entry
        # ----------------
        elif message["action"] == "kill":
            # TODO: Add a delete method for removing an entry from the list
            self.send(text_data=json.dumps({"error": 'Unsupported', "message": "This action is not supported. Please develop it!"}))


        # ----------------
        # Update some aspect of the current board
        # ----------------
        elif message["action"] == "update":
            # TODO: Add update method for handling HP updates
            # TODO: add update method for removing condition
            self.send(text_data=json.dumps({"error": 'Unsupported', "message": "This action is not supported. Please develop it!"}))


        # ----------------
        # Unexpected case. Report Error
        # ----------------
        else:
            self.send(text_data=json.dumps({"error": 'Failed to Parse Action', "message": message}))
