from enum import Enum

class Maturity(Enum):
    """
        Enum class representing the maturity stages of a plant.

        - SEED: The initial stage of a plant when it is a seed.
        - YOUNG: The stage where the plant has grown but is not yet fully mature.
        - ADULT: The mature stage of a plant, where it is fully grown and ready for reproduction.
    """
    SEED = "Seed"
    YOUNG = "Young"
    ADULT = "Adult"

class FinaleState(Enum):
    """
        Enum class representing the final states of a plant.

        - BLOOM: The plant is in a blooming state, potentially producing flowers or fruits.
        - FRUCTIFY: The plant has fructified, producing seeds or fruit for reproduction.
        - DEAD: The plant has died and can no longer grow or produce anything.
    """
    BLOOM = "Bloom"
    FRUCTIFY = "FRUCTIFY"
    DEAD = "DEAD"