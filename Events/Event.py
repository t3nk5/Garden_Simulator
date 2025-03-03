import random
from Events.Enum_events import EventType
from Events.Intensity import Intensity




class Event:
    def __init__(self):
        self.event_type  = self.random_event()
        self.intensity = self.random_intensity()


    @staticmethod
    def get_random_event() -> EventType:
        return random.choice(list(EventType))

    def random_event(self):
        event = self.get_random_event()
        print(f"OHH noo there is a : {event.name}")
        return event

    @staticmethod
    def random_intensity() -> Intensity:
        return random.choice(list(Intensity))


    def __str__(self) -> str:
        return (
            f"🌱 {self.event_type.name.capitalize()} \n"
            f"☠️ {self.intensity.name.capitalize()} \n"
        )


