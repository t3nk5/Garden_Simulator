import random
from typing import Optional

from Plants.Plant import Plant
from Maturity.Maturity import FinaleState, Maturity


class AppleTree(Plant):
    def __init__(self, water_requirements, light_requirements, fertilizer_required, speed_to_growth, health) -> None:
        super().__init__(water_requirements, light_requirements, fertilizer_required, speed_to_growth, health)
        self.name = "Apple Tree"
        self.maturity = Maturity.SEED
        self.FinaleState = FinaleState.FRUCTIFY
        self.actual_cut = 0

    def give_water(self, water) -> None:
        if super().check_water(water):
            self.water += water
            super().check_water_for_growth()
        else:
            pass

    def change_light(self, light) -> None:
        if super().check_light(light):
            self.light += light
            super().check_light_for_growth()
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
        if self.FinaleState == FinaleState.FRUCTIFY and self.maturity == Maturity.ADULT:
            nbr_seed = random.randint(1, 4)
            return self.name, nbr_seed



    def __str__(self) -> str:
        return (
            f"🌱 {self.name} \n"+
            super().__str__() +
            f"🤓 Maturity: {self.maturity.name}\n"
            f"🤓 Day: {self.day}\n"
        )