import random
from Events.Enum_events import EventType
from Events.Intensity import Intensity




class Event:
    """
        Class representing an event that affects the garden.
        Attributes:
            event_type (EventType): The type of the event (e.g., storm, drought).
            intensity (Intensity): The intensity of the event (e.g., very strong, mild).
    """
    def __init__(self):
        """
            Initializes the Event instance by assigning a random event type
            and a random intensity to the event.
       """
        self.event_type  = self.random_event()
        self.intensity = self.random_intensity()


    @staticmethod
    def get_random_event() -> EventType:
        """
            Returns a random event type from the EventType enum.
            Returns:
                EventType: A randomly selected event type (STORM, DROUGHT, etc.).
        """
        return random.choice(list(EventType))

    def random_event(self):
        """
            Randomly selects an event type and prints the event name.
            Returns:
                    EventType: The selected event type.
        """
        event = self.get_random_event()
        print(f"OHH noo there is a : {event.name}")
        return event

    @staticmethod
    def random_intensity() -> Intensity:
        """
            Returns a random intensity level from the Intensity enum.
            Returns:
                Intensity: A randomly selected intensity (VERY_GOOD, GOOD, etc.).
        """
        return random.choice(list(Intensity))


    def __str__(self) -> str:
        """
            Provides a string representation of the event, including its type
            and intensity.
            Returns:
                str: A formatted string with the event type and intensity.
        """
        return (
            f"🌱 {self.event_type.name.capitalize()} \n"
            f"☠️ {self.intensity.name.capitalize()} \n"
        )


