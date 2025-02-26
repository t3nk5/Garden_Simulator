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


    def add_day(self):
        pass








    def __str__(self) -> str:
        return (
            f"🌱 {self.name} \n"
            f"🌸 Color: {self.color}\n"
            f"📏 Size: {self.size}\n"
            f"💧 Water requirement: {self.water}/{self.water_requirements}\n"
            f"☀️ Light requirement: {self.light}/{self.light_requirements}\n"
            f"🌱 Fertilizer: {self.fertilizer}/{self.fertilizer_required}\n"
            f"⚡ Speed growth: {self.speed}/{self.speed_to_growth}\n"
            f"❤️ Health: {self.health}\n"
            f"🤓 Maturity: {self.maturity.name}\n"
        )