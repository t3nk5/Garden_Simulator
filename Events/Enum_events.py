from enum import Enum

class EventType(Enum):
    """
        Enum representing different types of events that can affect the garden.
        Attributes:
            STORM (int): A storm event that may damage plants.
            DROUGHT (int): A drought event that reduces water availability.
            PARASITE (int): A parasite invasion that affects plant health.
            DISEASE (int): A disease outbreak that can spread among plants.
    """
    STORM = 1
    DROUGHT = 2
    PARASITE = 3
    DISEASE = 4