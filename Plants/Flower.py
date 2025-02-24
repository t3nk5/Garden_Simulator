from Plants.Plant import Plant
from Maturity.maturity import FinaleState


class Flower(Plant):
    def __init__(self, water_requirements, light_requirements, fertilizer_required, speed_to_growth, health, color) -> None:
        super().__init__(water_requirements, light_requirements, fertilizer_required, speed_to_growth, health)
        self.FinaleState = FinaleState.BLOOM
        self.color = color


    def change_light(self, light) -> None:
        if super().check_light(light):
            self.light += light
            print(super().check_light_for_growth())
        else:
            pass

    def give_water(self, water) -> None:
        if super().check_water(water):
            self.water += water
            print(super().check_water_for_growth())
        else:
            pass

    def add_fertilizer(self, fertilizer) -> None:
        if super().check_fertilizer(fertilizer):
            self.fertilizer += fertilizer
            print(super().check_fertilizer_for_growth())
        else:
            pass










    def __str__(self) -> str:
        return f'Color: {self.color}\nSize: {self.size}\nWater requirement: {self.water}/{self.water_requirements}\nLight requirement: {self.light}/{self.light_requirements}\nFertilizer: {self.fertilizer}/{self.fertilizer_required}\nSpeed growth: {self.speed}/{self.speed_to_growth}'