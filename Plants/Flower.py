import random
from typing import Optional

from Plants.Plant import Plant
from Maturity.Maturity import FinaleState, Maturity


class Flower(Plant):
    """
        Represents a Flower plant in the garden game.
        Inherits from the Plant class and adds specific properties and methods for a flower, including
        growth and care (water, light, fertilizer), maturity tracking, and special attributes like color.
        Attributes:
            name (str): The name of the plant ("Flower").
            maturity (Maturity): The maturity stage of the flower (initially SEED).
            FinaleState (FinaleState): The final state of the flower (initially BLOOM).
            color (str): The color of the flower.
        Methods:
            change_light(light: int) -> None: Adds light to the flower's light value if valid and checks for growth.
            give_water(water: int) -> None: Adds water to the flower's water value if valid and checks for growth.
            add_fertilizer(fertilizer: int) -> None: Adds fertilizer to the flower's fertilizer value if valid and checks for growth.
            dead() -> None: Marks the flower as dead and prints a message.
            check_maturity() -> Optional[tuple[str, int]]: Checks if the flower has bloomed and returns the number of flowers produced.
            __str__() -> str: Returns a string representation of the flower's state, including its color, maturity, and other attributes.
    """

    def __init__(self, water_requirements, light_requirements, fertilizer_required, speed_to_growth, health, color) -> None:
        """
            Initializes a new Flower instance with the provided parameters.
            Args:
                water_requirements (int): The water required for the flower to grow.
                light_requirements (int): The light required for the flower to grow.
                fertilizer_required (int): The fertilizer required for the flower to grow.
                speed_to_growth (float): The speed at which the flower grows.
                health (int): The health of the flower.
                color (str): The color of the flower.
        """
        super().__init__(water_requirements, light_requirements, fertilizer_required, speed_to_growth, health)
        self.name = "Flower"
        self.maturity = Maturity.SEED
        self.FinaleState = FinaleState.BLOOM
        self.color = color


    def change_light(self, light) -> None:
        """
            Adds light to the flower if the amount is valid and checks for growth.
            Args:
                light (int): The amount of light to be added to the flower.
        """
        if super().check_light(light):
            self.light += light
            super().check_light_for_growth()
        else:
            pass

    def give_water(self, water) -> None:
        """
            Adds water to the flower if the amount is valid and checks for growth.
            Args:
                water (int): The amount of water to be added to the flower.
        """
        if super().check_water(water):
            self.water += water
            super().check_water_for_growth()
        else:
            pass

    def add_fertilizer(self, fertilizer) -> None:
        """
            Adds fertilizer to the flower if the amount is valid and checks for growth.
            Args:
                fertilizer (int): The amount of fertilizer to be added to the flower.
        """
        if super().check_fertilizer(fertilizer):
            self.fertilizer += fertilizer
            super().check_fertilizer_for_growth()
        else:
            pass

    def dead(self):
        """
            Marks the flower as dead and prints a message indicating it.
        """
        self.FinaleState = FinaleState.DEAD
        print(f"Your {self.name} is dead!")

    def check_maturity(self) -> Optional[tuple[str, int]]:
        """
            Checks if the flower is mature enough to bloom and produce seeds.
            Returns:
                A tuple containing the name of the flower and the number of seeds produced if the flower is mature and in bloom.
                None if the flower is not yet mature.
        """
        if self.FinaleState == FinaleState.BLOOM and self.maturity == Maturity.ADULT:
            nbr_flower = random.randint(1, 7)
            return self.name, nbr_flower



    def __str__(self) -> str:
        """
            Returns a string representation of the flower's current state.
            Returns:
                A string with the flower's name, color, maturity, health, and other important attributes.
        """
        return (
            f"🌱 {self.name} \n"
            f"♥️ {self.color} \n"+
            super().__str__() +
            f"🤓 Maturity: {self.maturity.name}\n"
            f"🤓 Day: {self.day}\n"
        )