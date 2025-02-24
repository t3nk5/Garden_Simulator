from enum import Enum

class Maturity(Enum):
    SEED = "Seed"
    YOUNG = "Young"
    ADULT = "Adult"

class FinaleState(Enum):
    BLOOM = "Bloom"
    FRUCTIFY = "FRUCTIFY"
    DEAD = "DEAD"