import random
from typing import Optional

from Plants.Plant import Plant
from Maturity.Maturity import FinaleState, Maturity

class Salad(Plant):
    """
        A subclass of Plant representing a Salad plant.
        This class implements the specific behavior of a Salad plant, including water, light, and fertilizer
        requirements, growth speed, maturity checks, and handling of its final state (e.g., being dead or producing seeds).
        Attributes:
            FinaleState (FinaleState): The final state of the plant (whether it is dead or has bloomed).
            name (str): The name of the plant ("Salad").
            maturity (Maturity): The current maturity state of the plant (e.g., seed, young, adult).
        Methods:
            give_water(water: int) -> None: Provides water to the plant if it is within the valid range.
            change_light(light: int) -> None: Provides light to the plant if it is within the valid range.
            add_fertilizer(fertilizer: int) -> None: Adds fertilizer to the plant if it is within the valid range.
            dead() -> None: Sets the plant's final state to dead and notifies the user.
            check_maturity() -> Optional[tuple[str, int]]: Checks if the plant has reached its final state and is ready to produce seeds.
            __str__() -> str: Returns a string representation of the plant, including its growth, maturity, and health.
    """

    def __init__(self, water_requirements, light_requirements, fertilizer_required, speed_to_growth, health) -> None:
        """
            Initializes the Salad plant with specific growth requirements and sets its initial state.
            Args:
                water_requirements (int): The amount of water required for the Salad to grow.
                light_requirements (int): The amount of light required for the Salad to grow.
                fertilizer_required (int): The amount of fertilizer needed for the Salad.
                speed_to_growth (float): The rate at which the Salad plant grows.
                health (int): The initial health of the plant.
        """
        super().__init__(water_requirements, light_requirements, fertilizer_required, speed_to_growth, health)
        self.name = "Salad"
        self.maturity = Maturity.SEED
        self.FinaleState = FinaleState.BLOOM

    def give_water(self, water) -> None:
        """
            Provides water to the Salad plant, adjusting its growth speed.
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
            Changes the light exposure for the Salad plant, adjusting its growth speed.
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
            Adds fertilizer to the Salad plant, adjusting its growth speed.
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
            Checks if the Salad plant has reached its final mature state and produces seeds if ready.
            Returns:
                 Optional[tuple[str, int]]: A tuple with the plant's name and the number of seeds if mature,
                 or None if not mature.
        """
        if self.FinaleState == FinaleState.FRUCTIFY and self.maturity == Maturity.ADULT:
            nbr_seed = random.randint(1, 2)
            return self.name, nbr_seed

    def __str__(self) -> str:
        """
            Returns a string representation of the Salad plant's current state, including its size, water, light,
            fertilizer levels, growth speed, health, maturity, and the current day.
            Returns:
                str: A string describing the Salad plant's attributes.
        """
        return (
            f"🌱 {self.name} \n"+
            super().__str__() +
            f"🤓 Maturity: {self.maturity.name}\n"
            f"🤓 Day: {self.day}\n"
        )