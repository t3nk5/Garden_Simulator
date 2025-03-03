import random
from typing import Optional

from Plants.Plant import Plant
from Maturity.maturity import FinaleState, Maturity


class Flower(Plant):
    def __init__(self, water_requirements, light_requirements, fertilizer_required, speed_to_growth, health, color) -> None:
        super().__init__(water_requirements, light_requirements, fertilizer_required, speed_to_growth, health)
        self.name = "Flower"
        self.maturity = Maturity.SEED
        self.FinaleState = FinaleState.BLOOM
        self.color = color


    def change_light(self, light) -> None:
        if super().check_light(light):
            self.light += light
            super().check_light_for_growth()
        else:
            pass

    def give_water(self, water) -> None:
        if super().check_water(water):
            self.water += water
            super().check_water_for_growth()
        else:
            pass

    def add_fertilizer(self, fertilizer) -> None:
        if super().check_fertilizer(fertilizer):
            self.fertilizer += fertilizer
            super().check_fertilizer_for_growth()
        else:
            pass

    def dead(self):
        self.FinaleState = FinaleState.DEAD

    def check_maturity(self) -> Optional[tuple[str, int]]:
        if self.FinaleState == FinaleState.BLOOM and self.maturity == Maturity.ADULT:
            nbr_flower = random.randint(1, 7)
            return self.name, nbr_flower



    def __str__(self) -> str:
        return (
            f"🌱 {self.name} \n"
            f"♥️ {self.color} \n"+
            super().__str__() +
            f"🤓 Maturity: {self.maturity.name}\n"
            f"🤓 Day: {self.day}\n"
        )