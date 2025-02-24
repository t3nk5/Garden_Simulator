from abc import ABC,abstractmethod


class Plant(ABC):
    def __init__(self, water_requirements, light_requirements, fertilizer_required, speed_to_growth, health) -> None:
        self.water_requirements = water_requirements
        self.light_requirements = light_requirements
        self.speed_to_growth = speed_to_growth
        self.fertilizer_required = fertilizer_required
        self.health = health
        self.water = 0
        self.light = 0
        self.speed = 0
        self.size = 0
        self.fertilizer = 0
        self.cut = 0

    @abstractmethod
    def give_water(self, water) -> None:
        pass

    @staticmethod
    def check_water(water) -> bool: return 0 < water < 11

    def check_water_for_growth(self):
        diff = abs(self.water - self.water_requirements)

        if diff > 5:
            self.speed = self.speed_to_growth*0
        elif diff >= 3:
            self.speed = self.speed_to_growth *0.5
        elif diff <= 1:
            self.speed = self.speed_to_growth

    @abstractmethod
    def change_light(self, fertilizer) -> None:
        pass

    @staticmethod
    def check_light(light)-> bool: return 0 < light < 15

    def check_light_for_growth(self):
        diff = abs(self.light - self.light_requirements)

        if diff > 5:
            self.speed = self.speed_to_growth*0
        elif diff >= 3:
            self.speed = self.speed_to_growth *0.5
        elif diff <= 1:
            self.speed = self.speed_to_growth

    @abstractmethod
    def add_fertilizer(self, fertilizer) -> None:
        pass

    @staticmethod
    def check_fertilizer(fertilizer) -> bool: return 0 < fertilizer < 5

    def check_fertilizer_for_growth(self):
        diff = abs(self.fertilizer - self.fertilizer_required)

        if diff > 5:
            self.speed = self.speed_to_growth * 0
        elif diff >= 3:
            self.speed = self.speed_to_growth * 0.5
        elif diff <= 1:
            self.speed = self.speed_to_growth


    def cut_plant(self):
        if self.cut == 0:
            self.speed *= 1.01
            self.cut = 8
        else:
            print("You can't cut")
