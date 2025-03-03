from enum import Enum

class CREATE_PLANTS(Enum):
    """
        Enum class representing different types of plants that can be created.

        - TREE: Represents a tree plant that can be grown.
        - FLOWER: Represents a flower plant that can be grown.
        - SALAD: Represents a salad plant that can be grown.
        """
    TREE = 1
    FLOWER = 2
    SALAD = 3