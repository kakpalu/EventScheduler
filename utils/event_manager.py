import json

from models.event import Event
from utils.utils import json_serial


class EventScheduler:
    event_file = "models/events.json"

    def __init__(self):
        self.events = []
        self.load_events()

    def add_event(self, title, date, description=""):
        event = Event(title, date, description)
        self.events.append(event)
        self.sort_events()
        self.save_events()

    def remove_event(self, title):
        for event in self.events:
            if event.title == title:
                self.events.remove(event)
                self.save_events()
                return True
        return False

    def list_events(self):
        if not self.events:
            print("No events scheduled.")
        else:
            return self.events

    def sort_events(self):
        self.events.sort(key=lambda x: x.date)

    def save_events(self):
        with open(self.event_file, 'w') as file:

            json_object = []
            for event in self.events:
                json_object.append({
                    "title": event.title,
                    "date": event.date.strftime("%Y-%m-%d"),
                    "description": event.description
                })
            json.dump(json_object, file, default=json_serial)

    def load_events(self):
        try:
            with open(self.event_file, 'r') as file:
                data = json.load(file)
                self.events = [Event(**event_data) for event_data in data]
                self.sort_events()
        except FileNotFoundError:
            print("No events file found. Starting with an empty scheduler.")
            # create a event.json file for data storage
            with open(self.event_file, 'w') as file:
                # add basic data to the file
                file.write("[]")
        except json.JSONDecodeError:
            self.events = []

    def print_events(self):
        if not self.events:
            print("No events scheduled.")
        for event in self.events:
            print(event)

