from abc import ABC,abstractmethod

from Maturity.maturity import Maturity, FinaleState

@abstractmethod
class Plant(ABC):
    def __init__(self, water_requirements, light_requirements, fertilizer_required, speed_to_growth, health) -> None:
        self.water_requirements = water_requirements
        self.light_requirements = light_requirements
        self.speed_to_growth = speed_to_growth
        self.fertilizer_required = fertilizer_required
        self.health = health
        self.maturity = Maturity.SEED
        self.water = 0
        self.light = 0
        self.speed = 0
        self.size = 0
        self.fertilizer = 0
        self.cut = 0
        self.name = "Plant"
        self.day = 0



    def get_name(self) -> str:
        return f"{self.name}\n"

    @abstractmethod
    def give_water(self, water) -> None:
        pass

    @staticmethod
    def check_water(water) -> bool: return 0 < water < 11

    def check_water_for_growth(self) -> None:
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

    def check_light_for_growth(self) -> None:
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
    def check_fertilizer(fertilizer) -> bool: return 0 < fertilizer < 10

    def check_fertilizer_for_growth(self) -> None:
        diff = abs(self.fertilizer - self.fertilizer_required)

        if diff > 5:
            self.speed = self.speed_to_growth * 0
        elif diff >= 3:
            self.speed = self.speed_to_growth * 0.5
        elif diff <= 1:
            self.speed = self.speed_to_growth

    def cut_plant(self) -> bool:
        if self.check_cut_plant():
            self.cut_plant_for_growth()
            self.cut = 6
            return True
        else:
            print("You can't cut plant")
            return False

    def cut_plant_for_growth(self):
            self.speed *= 1.04


    def check_cut_plant(self) -> bool:
        return self.cut == 0

    def change_maturity(self, maturity) -> None:
        self.maturity = maturity


    def check_day(self):
        if self.day >= 15:
            self.maturity = Maturity.YOUNG
        if self.day >=30:
            self.maturity = Maturity.ADULT


    def pass_day(self):
        self.day += 1
        self.check_day()
        self.size += self.speed

    @abstractmethod
    def dead(self):
        pass

    def check_is_dead(self) -> bool:
        if self.health <=0:
            self.dead()
            return True
        else:
            return False
