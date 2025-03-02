from Plants.Plant import Plant
from Maturity.maturity import FinaleState, Maturity


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


    def __str__(self) -> str:
        return (
            f"🌱 {self.name} \n"
            f"📏 Size: {self.size}\n"
            f"💧 Water requirement: {self.water}/{self.water_requirements}\n"
            f"☀️ Light requirement: {self.light}/{self.light_requirements}\n"
            f"🌱 Fertilizer: {self.fertilizer}/{self.fertilizer_required}\n"
            f"⚡ Speed growth: {self.speed}/{self.speed_to_growth}\n"
            f"❤️ Health: {self.health}\n"
            f"🤓 Maturity: {self.maturity.name}\n"
            f"🤓 Day: {self.day}\n"
        )