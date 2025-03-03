import random
from typing import Optional
from abc import ABC,abstractmethod

from Maturity.Maturity import Maturity

@abstractmethod
class Plant(ABC):
    """
        Abstract base class for all types of plants.
        This class represents a general plant that requires water, light, and fertilizer for growth. It includes
        methods for managing plant care, checking growth status, and handling maturity and health. It is meant to be inherited
        by specific plant types (like flowers, trees, etc.) which will implement plant-specific behavior.
    Attributes:
        water_requirements (int): The amount of water the plant needs to grow.
        light_requirements (int): The amount of light the plant needs to grow.
        speed_to_growth (float): The rate at which the plant grows.
        fertilizer_required (int): The amount of fertilizer required for optimal growth.
        health (int): The current health of the plant.
        maturity (Maturity): The current maturity stage of the plant.
        water (int): The current water level of the plant.
        light (int): The current light level of the plant.
        speed (float): The current speed of the plant's growth.
        size (float): The size of the plant.
        fertilizer (int): The current fertilizer level of the plant.
        cut (int): Whether the plant has been cut or not.
        name (str): The name of the plant (initialized as "Plant").
        day (int): The current day of the plant's life.
    Methods:
        get_name() -> str: Returns the name of the plant.
        give_water(water: int) -> None: Abstract method to give water to the plant.
        change_light(light: int) -> None: Abstract method to change the light for the plant.
        add_fertilizer(fertilizer: int) -> None: Abstract method to add fertilizer to the plant.
        check_water(water: int) -> bool: Static method to check if the provided water amount is valid.
        check_water_for_growth() -> None: Checks and adjusts the growth speed based on the water level.
        check_light(light: int) -> bool: Static method to check if the provided light level is valid.
        check_light_for_growth() -> None: Checks and adjusts the growth speed based on the light level.
        check_fertilizer(fertilizer: int) -> bool: Static method to check if the provided fertilizer amount is valid.
        check_fertilizer_for_growth() -> None: Checks and adjusts the growth speed based on the fertilizer level.
        cut_plant() -> bool: Tries to cut the plant and increase its growth speed if successful.
        check_cut_plant() -> bool: Checks if the plant can be cut (it hasn't been cut yet).
        check_day() -> None: Updates the plant's maturity based on the number of days passed.
        new_day() -> None: Simulates the passage of a day, reducing water and fertilizer levels.
        lower_health(nbr: int) -> None: Reduces the plant's health by the specified amount.
        check_health() -> None: Checks the health of the plant based on the water levels and applies damage.
        check_light_health() -> None: Checks the plant's health based on the light levels and applies damage.
        check_fertilizer_health() -> None: Checks the plant's health based on the fertilizer levels and applies damage.
        pass_day() -> None: Advances the plant by one day, updating maturity, growth, and health.
        check_is_dead() -> bool: Checks if the plant is dead based on health.
        check_maturity() -> Optional[tuple[str, int]]: Abstract method to check the plant's maturity and return a result.
        dead() -> None: Abstract method to handle the plant's death.
        __str__() -> str: Returns a string representation of the plant's current state.
    """

    def __init__(self, water_requirements, light_requirements, fertilizer_required, speed_to_growth, health) -> None:
        """
            Initializes the general attributes of a plant.
            Args:
                water_requirements (int): The amount of water the plant needs.
                light_requirements (int): The amount of light the plant needs.
                fertilizer_required (int): The amount of fertilizer the plant requires.
                speed_to_growth (float): The speed at which the plant grows.
                health (int): The health of the plant (starting health).
        """
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
        """
            Returns the name of the plant.
            Returns:
                str: The name of the plant.
        """
        return f"{self.name}\n"

    @abstractmethod
    def give_water(self, water) -> None:
        """
            Abstract method to provide water to the plant.
            Args:
                water (int): The amount of water to give to the plant.
        """
        pass

    @staticmethod
    def check_water(water) -> bool:
        """
            Checks if the given water amount is valid (between 1 and 10).
            Args:
                water (int): The amount of water to check.
            Returns:
                bool: True if valid, False otherwise.
        """
        return 0 < water < 11

    def check_water_for_growth(self) -> None:
        """
            Adjusts the growth speed based on the difference between the current water and the required water.
        """
        diff = abs(self.water - self.water_requirements)

        if diff > 5:
            self.speed = self.speed_to_growth*0
        elif diff >= 3:
            self.speed = self.speed_to_growth *0.5
        elif diff <= 1:
            self.speed = self.speed_to_growth

    @abstractmethod
    def change_light(self, fertilizer) -> None:
        """
            Abstract method to change the light conditions for the plant.
            Args:
                fertilizer (int): The amount of light to change.
        """
        pass

    @staticmethod
    def check_light(light)-> bool:
        """
            Checks if the given light amount is valid (between 1 and 14).
            Args:
                light (int): The amount of light to check.
            Returns:
                bool: True if valid, False otherwise.
        """
        return 0 < light < 15

    def check_light_for_growth(self) -> None:
        """
            Adjusts the growth speed based on the difference between the current light and the required light.
        """
        diff = abs(self.light - self.light_requirements)

        if diff > 5:
            self.speed = self.speed_to_growth*0

        elif diff >= 3:
            self.speed = self.speed_to_growth *0.5
        elif diff <= 1:
            self.speed = self.speed_to_growth

    @abstractmethod
    def add_fertilizer(self, fertilizer) -> None:
        """
            Abstract method to add fertilizer to the plant.
            Args:
                fertilizer (int): The amount of fertilizer to add to the plant.
        """
        pass

    @staticmethod
    def check_fertilizer(fertilizer) -> bool:
        """
            Checks if the given fertilizer amount is valid (between 1 and 9).
            Args:
                fertilizer (int): The amount of fertilizer to check.
            Returns:
                bool: True if valid, False otherwise.
        """
        return 0 < fertilizer < 10

    def check_fertilizer_for_growth(self) -> None:
        """
            Adjusts the growth speed based on the difference between the current fertilizer and the required fertilizer.
        """
        diff = abs(self.fertilizer - self.fertilizer_required)

        if diff > 5:
            self.speed = self.speed_to_growth * 0
        elif diff >= 3:
            self.speed = self.speed_to_growth * 0.5
        elif diff <= 1:
            self.speed = self.speed_to_growth

    def cut_plant(self) -> bool:
        """
            Attempts to cut the plant, which may increase its growth speed.
            Returns:
                bool: True if successful, False otherwise.
        """
        if self.check_cut_plant():
            self.cut_plant_for_growth()
            self.cut = 6
            return True
        else:
            print("You can't cut plant")
            return False

    def cut_plant_for_growth(self):
        """
            Checks if the plant can be cut (i.e., it hasn't been cut already).
            Returns:
                bool: True if the plant can be cut, False otherwise.
        """
        self.speed *= 1.04

    def check_cut_plant(self) -> bool:
        """
            Checks if the plant can be cut (i.e., it hasn't been cut already).
            Returns:
                bool: True if the plant can be cut, False otherwise.
        """
        return self.cut == 0

    def check_day(self):
        """
            Updates the plant's maturity based on the number of days passed.
        """
        if self.day >= 5:
            self.maturity = Maturity.YOUNG
        if self.day >=10:
            self.maturity = Maturity.ADULT

    def new_day(self):
        """
            Simulates the passing of a new day by reducing water and fertilizer levels.
        """
        if self.water - random.randint(1,2) < 0:
            self.water = 0
        else:
            self.water -= random.randint(1, 2)

        if self.fertilizer - random.randint(1,2) < 0:
            self.fertilizer = 0
        else:
            self.fertilizer -= random.randint(1,2)

    def lower_health(self, nbr):
        """
            Reduces the plant's health by a specified amount.
            Args:
                nbr (int): The amount to reduce the health by.
        """
        if self.health - nbr <= 0:
            self.health = 0
            self.dead()
        else:
            self.health -= nbr

    def check_health(self):
        """
            Checks and adjusts the plant's health based on its water levels.
        """
        diff_water = abs(self.water - self.water_requirements)
        self.lower_health(diff_water)
        if diff_water >= 3:
            print(f"You should give your {self.name} water\n")
        elif diff_water >= 5:
            print(f"You should give your {self.name} plenty of water\n")
        elif diff_water >= 15:
            print(f"Your {self.name} will die\n")

    def check_light_health(self):
        """
            Checks and adjusts the plant's health based on its light levels.
        """
        diff_light = abs(self.light - self.light_requirements)
        self.lower_health(diff_light)
        if diff_light <= 1:
            pass
        elif diff_light <= 3:
            print(f"You should change the light of your {self.name}\n")
        elif diff_light >= 5:
            print(f"Your {self.name} will die\n")

    def check_fertilizer_health(self):
        """
            Checks and adjusts the plant's health based on its fertilizer levels.
        """
        diff_fertilizer = abs(self.fertilizer - self.fertilizer_required)
        self.lower_health(diff_fertilizer)
        if diff_fertilizer <= 1:
            pass
        elif diff_fertilizer <= 3:
            print(f"You should change the volume of fertilizer of your {self.name}\n")
        elif diff_fertilizer >= 5:
            print(f"Your {self.name} will die\n")

    def pass_day(self):
        """
            Advances the plant by one day, updating maturity, size, and health.
        """
        self.day += 1
        self.check_day()
        self.size += self.speed
        self.new_day()
        self.check_health()
        self.check_light_health()
        self.check_fertilizer_health()

    @abstractmethod
    def dead(self):
        """
            Abstract method to handle the plant's death.
        """
        pass

    def check_is_dead(self) -> bool:
        """
            Checks if the plant is dead based on its health.
            Returns:
                bool: True if the plant is dead, False otherwise.
        """
        if self.health <=0:
            self.dead()
            return True
        else:
            return False

    @abstractmethod
    def check_maturity(self) -> Optional[tuple[str, int]]:
        """
            Abstract method to check the plant's maturity and return a result.
            Returns:
                Optional[tuple[str, int]]: A tuple with the plant's name and the number of items produced (e.g., fruits, flowers).
        """
        pass

    def __str__(self) -> str:
        """
            Returns a string representation of the plant's current state.
            Returns:
                str: The plant's attributes, including size, water, light, fertilizer, growth speed, and health.
        """
        return (
        f"📏 Size: {self.size}\n"
        f"💧 Water requirement: {self.water}/{self.water_requirements}\n"
        f"☀️ Light requirement: {self.light}/{self.light_requirements}\n"
        f"🌱 Fertilizer: {self.fertilizer}/{self.fertilizer_required}\n"
        f"⚡ Speed growth: {self.speed}/{self.speed_to_growth}\n"
        f"❤️ Health: {self.health}\n"
        )