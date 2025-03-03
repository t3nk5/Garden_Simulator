from enum import Enum


class Intensity(Enum):
    """
        Enum representing the intensity levels of an event or action in the game.
        Attributes:
            VERY_EASY (int): Represents a very easy intensity level (value: 2).
            EASY (int): Represents an easy intensity level (value: 4).
            HARD (int): Represents a hard intensity level (value: 6).
            VERY_HARD (int): Represents a very hard intensity level (value: 8).
    """
    VERY_EASY = 2
    EASY = 4
    HARD = 6
    VERY_HARD = 8


