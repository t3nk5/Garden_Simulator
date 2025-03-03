import random
from typing import Optional

from Plants.Plant import Plant
from Maturity.Maturity import FinaleState, Maturity


class AppleTree(Plant):
    """
        A subclass of Plant representing an Apple Tree.
        This class simulates an Apple Tree, with specific requirements for water, light, and fertilizer.
        It grows over time, eventually producing seeds once it reaches the 'ADULT' maturity state.
        Attributes:
            FinaleState (FinaleState): The final state of the plant (whether it is dead, bloomed, or fructified).
            name (str): The name of the plant ("Apple Tree").
            maturity (Maturity): The current maturity state of the plant (e.g., seed, young, adult).
            actual_cut (int): Counter to track if the plant has been cut or not.
        Methods:
            give_water(water: int) -> None: Provides water to the plant if it is within the valid range.
            change_light(light: int) -> None: Provides light to the plant if it is within the valid range.
            add_fertilizer(fertilizer: int) -> None: Adds fertilizer to the plant if it is within the valid range.
            dead() -> None: Sets the plant's final state to dead and prints a message indicating the plant is dead.
            check_maturity() -> Optional[tuple[str, int]]: Checks if the plant has reached its final state and is ready to produce seeds.
            __str__() -> str: Returns a string representation of the plant's current state, including its growth, maturity, and health.
    """

    def __init__(self, water_requirements, light_requirements, fertilizer_required, speed_to_growth, health) -> None:
        """
            Initializes the AppleTree with specific growth requirements and sets its initial state.
            Args:
                water_requirements (int): The amount of water required for the AppleTree to grow.
                light_requirements (int): The amount of light required for the AppleTree to grow.
                fertilizer_required (int): The amount of fertilizer needed for the AppleTree.
                speed_to_growth (float): The rate at which the AppleTree grows.
                health (int): The initial health of the plant.
        """
        super().__init__(water_requirements, light_requirements, fertilizer_required, speed_to_growth, health)
        self.name = "Apple Tree"
        self.maturity = Maturity.SEED
        self.FinaleState = FinaleState.FRUCTIFY
        self.actual_cut = 0

    def give_water(self, water) -> None:
        """
            Provides water to the AppleTree, adjusting its growth speed.
            Args:
                water (int): The amount of water to give to the plant.
        """
        if super().check_water(water):
            self.water += water
            super().check_water_for_growth()
        else:
            pass

    def change_light(self, light) -> None:
        """
            Changes the light exposure for the AppleTree, adjusting its growth speed.
            Args:
                light (int): The amount of light to provide to the plant.
        """
        if super().check_light(light):
            self.light += light
            super().check_light_for_growth()
        else:
            pass

    def add_fertilizer(self, fertilizer) -> None:
        """
            Adds fertilizer to the AppleTree, adjusting its growth speed.
            Args:
                fertilizer (int): The amount of fertilizer to add to the plant.
        """
        if super().check_fertilizer(fertilizer):
            self.fertilizer += fertilizer
            super().check_fertilizer_for_growth()
        else:
            pass

    def dead(self):
        """
            Sets the plant's final state to dead and prints a message indicating the plant is dead.
        """
        self.FinaleState = FinaleState.DEAD
        print(f"Your {self.name} is dead!")

    def check_maturity(self) -> Optional[tuple[str, int]]:
        """
            Checks if the AppleTree has reached its final mature state and produces seeds if ready.
            Returns:
                Optional[tuple[str, int]]: A tuple with the plant's name and the number of seeds if mature,
                or None if not mature.
        """
        if self.FinaleState == FinaleState.FRUCTIFY and self.maturity == Maturity.ADULT:
            nbr_seed = random.randint(1, 4)
            return self.name, nbr_seed

    def __str__(self) -> str:
        """
            Returns a string representation of the AppleTree's current state, including its size, water, light,
            fertilizer levels, growth speed, health, maturity, and the current day.
            Returns:
                str: A string describing the AppleTree's attributes.
        """
        return (
            f"🌱 {self.name} \n"+
            super().__str__() +
            f"🤓 Maturity: {self.maturity.name}\n"
            f"🤓 Day: {self.day}\n"
        )