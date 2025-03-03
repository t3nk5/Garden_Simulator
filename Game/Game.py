import os

import Utils
import json
from Garden import Garden
from Utils import choose_action
from Events.Event import Event
from Plants.Plant import Plant
from Plants.Tree import AppleTree
from Plants.Flower import Flower
from Plants.Salad import Salad
from Plants.Enum_Plant import CREATE_PLANTS
from Maturity.Maturity import Maturity, FinaleState


class Game:
    """
        A class representing the game itself, including the player's progress, garden, and various actions.
    """

    def __init__(self, name_player:str) -> None:
        """
            Initializes the game with the player's name and sets up the game state such as money, actions, and seeds.
            Args:
                name_player (str): The name of the player.
        """
        self.name_player = name_player
        self.garden: Garden | None = None
        self.action = 4
        self.money = 0
        self.seeds = {}

    def display_garden(self) -> None:
        """
            Displays the current state of the player's garden, including the health and other attributes of the plants.
            Iterates through the plants and prints their status.
        """
        print("\n\nHere is your garden now:\n")
        nbr_plant = 0
        for plant in self.garden.plants:
            if not plant.health<= 0:
                print(plant.__str__())
                print("---------------------------")
                nbr_plant += 1
        if nbr_plant <= 0:
            print("No plant available")

    def start(self, NUMBER_OF_PLANTS) -> None:
        """
            Starts a new game and initializes the garden with a specified number of plants.
            Args:
                NUMBER_OF_PLANTS (int): The number of plants to start the garden with.
        """
        list_temp = Utils.choose_plants_to_beginning(NUMBER_OF_PLANTS)
        self.garden = Garden(list_temp)

    def sell_seed(self) -> None:
        """
            Allows the player to sell a seed from their inventory. Updates the player's money and seed count.
        """
        seed_list = list(self.seeds.items())
        for index, (seed, quantity) in enumerate(seed_list, start=1):
            print(f"{index}. {seed}: {quantity} seeds")

            print("\nEnter the number of the seed type you want to sell: ")
            choice:int = Utils.get_valid_number(len(seed_list))
            seed_name = seed_list[choice - 1][0]
            self.seeds[seed_name] -= 1
            print(f"You sold 1 {seed_name} seed.")
            self.money += 10
            print(f"You have now {self.money} money.")
            if self.seeds[seed_name] == 0:
                del self.seeds[seed_name]
                print(f"You no longer have any {seed_name} seeds.")

    def display_seeds(self) -> None:
        """
            Displays all the seeds the player currently has in their inventory, grouped by seed type.
            Calls the `sell_seed()` method for the player to sell a seed.
        """
        if len(self.seeds) == 0:
            print("You don't have any seeds yet.")
        else:
            print("\nWhich plant seeds you want to sell ?\n")
            seed_count = {}
            for seed, quantity in self.seeds.items():
                if seed in seed_count:
                    seed_count[seed] += quantity
                else:
                    seed_count[seed] = quantity
            for seed, total_quantity in seed_count.items():
                print(f"{seed}: {total_quantity} seeds")
        self.sell_seed()

    @staticmethod
    def check_health_plant(plant: Plant, intensity: int) -> None:
        """
            Checks and adjusts the health of a plant based on the intensity of an event.
            Args:
                plant (Plant): The plant whose health needs to be checked.
                intensity (int): The intensity of the event affecting the plant's health.
        """
        if plant.health - intensity < 0:
            plant.health = 0
        else:
            plant.health -= intensity

    def event(self, event: Event) -> None:
        """
            Handles the effects of a specific event (e.g., storm, drought) on all plants in the garden.
            Args:
               event (Event): The event that will affect the plants.
        """
        intensity = event.intensity
        if event.event_type == event.event_type.STORM:
            for plant in self.garden.plants:
                plant.water += intensity.value
                self.check_health_plant(plant, intensity.value)
        elif event.event_type == event.event_type.DROUGHT:
            for plant in self.garden.plants:
                if plant.water - intensity.value <0:
                    plant.water -= 0
                else:
                    plant.water -= intensity.value
                    self.check_health_plant(plant, intensity.value)
        elif event.event_type == event.event_type.PARASITE:
            for plant in self.garden.plants:
                self.check_health_plant(plant, intensity.value *2)
        elif event.event_type == event.event_type.DISEASE:
            for plant in self.garden.plants:
                self.check_health_plant(plant, intensity.value)

    def add_day(self) -> None:
        """
            Advances the game by one day, allowing plants to mature and produce seeds.
        """
        if self.action <= 1:
            for plant in self.garden.plants:
                plant.pass_day()
                result = plant.check_maturity()
                if result:
                    name_plant, quantity = result
                    if name_plant in self.seeds:
                        self.seeds[name_plant] += quantity
                    else:
                        self.seeds[name_plant] = quantity

                    print(f"Your {name_plant} produced {quantity} seeds\n")

    def is_finished(self) -> bool:
        """
            Checks if the game is finished (i.e., if no plants are alive).
            Returns:
                bool: True if no plants are alive, otherwise False
        """
        nbr_plant_alive = 0
        for plant in self.garden.plants:
            if plant.check_is_dead():
                pass
            else:
                nbr_plant_alive += 1
        return nbr_plant_alive <= 0

    def use_action(self):
        """
            Uses one of the player's available actions. If there are no actions left, a new day starts.
        """
        if self.check_action():
            self.action -=1
            print(f"You have left {self.action} action today !")
        else:
            self.add_day()
            print(f"This is a new day !")
            self.action = 4

    def check_action(self) -> bool:
        """
            Checks if the player has actions left for the current day.
            Returns:
                bool: True if actions left, otherwise False.
        """
        return self.action > 1

    def buy_plant(self):
        """
            Allows the player to buy a new plant from the available options (Apple Tree or Flower).
        """
        print("\nWhich plant plant you want to buy?")
        for plant in CREATE_PLANTS:
            print(f"{plant.name}")
        result = Utils.get_valid_number(len(CREATE_PLANTS))
        if result == 1:
            self.garden + AppleTree(5, 7, 4, 0.07, 150)
        elif result == 2:
            self.garden + Flower(5, 10, 5, 0.2, 50, "blue")

    def save(self, filename:str) -> None:
        """
            Saves the current game state (money, actions, seeds, garden) to a JSON file.
            Args:
                filename (str): The filename where the game data will be saved.
        """
        data = {
            "player_name": self.name_player,
            "money": self.money,
            "action": self.action,
            "seeds": self.seeds,
            "garden": {
                "plants": [
                    {
                        "name": plant.name,
                        "water_requirements": plant.water_requirements,
                        "light_requirements": plant.light_requirements,
                        "speed_to_growth": plant.speed_to_growth,
                        "fertilizer_required": plant.fertilizer_required,
                        "health": plant.health,
                        "maturity": plant.maturity.name,  # Enum en string
                        "water": plant.water,
                        "light": plant.light,
                        "speed": plant.speed,
                        "size": plant.size,
                        "fertilizer": plant.fertilizer,
                        "cut": plant.cut,
                        "FinaleState": plant.FinaleState.name,  # Enum en string
                        "day": plant.day
                    }
                    for plant in self.garden.plants
                ]
            }
        }

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

        print("Game saved successfully!")
        exit()


    def choose_action(self) -> None:
        action = Utils.choose_action()

        if action == 1:
            print("\nGive water to which plant ?")
            self.garden.get_name_plants()
            result = Utils.get_valid_number(len(self.garden.plants))
            selected_plant = self.garden.plants[result - 1]
            print(selected_plant.__str__())
            nbr_water = Utils.get_valid_number(10)
            selected_plant.give_water(nbr_water)
            self.use_action()
        elif action == 2:
            print("\nChange light to which plant ?")
            self.garden.get_name_plants()
            result = Utils.get_valid_number(len(self.garden.plants))
            selected_plant = self.garden.plants[result - 1]
            print(selected_plant.__str__())
            nbr_light = Utils.get_valid_number(10)
            selected_plant.change_light(nbr_light)
            self.use_action()
        elif action == 3:
            print("\nAdd fertilizer to which plant ?")
            self.garden.get_name_plants()
            result = Utils.get_valid_number(len(self.garden.plants))
            selected_plant = self.garden.plants[result - 1]
            print(selected_plant.__str__())
            fertilizer = Utils.get_valid_number(10)
            selected_plant.add_fertilizer(fertilizer)
            self.use_action()
        elif action == 4:
            print("\nwhich plant do you want to cut ?")
            self.garden.get_name_plants()
            result = Utils.get_valid_number(len(self.garden.plants))
            selected_plant = self.garden.plants[result - 1]
            print(selected_plant.__str__())
            if selected_plant.cut_plant():
                self.use_action()
                pass
            else: choose_action()

        elif action == 5:
            self.display_seeds()
            self.use_action()

        elif action == 6:
            if self.money <=0:
                print("You don't have enough money!")
                self.choose_action()
            else:
                print(f"\nYou have {self.money} money.\nWhat would you like to buy?\n")
                self.buy_plant()
        elif action == 7:
            self.save(f"{self.name_player}.json")

    def load_game(self) -> bool:
        filename = f"{self.name_player}.json"

        if os.path.exists(filename):
            choice = input(f"Save file found for {self.name_player}. Load it? (yes/no): ").strip().lower()

            if choice == "yes":
                try:
                    with open(filename, "r") as file:
                        data = json.load(file)
                    self.money = data["money"]
                    self.action = data["action"]
                    self.seeds = data["seeds"]
                    self.garden = Garden(plants=[])

                    for plant_data in data["garden"]["plants"]:
                        plant_name = plant_data["name"]

                        if plant_name == "Flower":
                            plant = Flower(
                                water_requirements=plant_data["water_requirements"],
                                light_requirements=plant_data["light_requirements"],
                                speed_to_growth=plant_data["speed_to_growth"],
                                fertilizer_required=plant_data["fertilizer_required"],
                                health=plant_data["health"],
                                color=plant_data.get("color", "unknown")
                            )
                        elif plant_name == "Apple Tree":
                            plant = AppleTree(
                                water_requirements=plant_data["water_requirements"],
                                light_requirements=plant_data["light_requirements"],
                                speed_to_growth=plant_data["speed_to_growth"],
                                fertilizer_required=plant_data["fertilizer_required"],
                                health=plant_data["health"]
                            )
                        elif plant_name == "Salad":
                            plant = Salad(
                                water_requirements=plant_data["water_requirements"],
                                light_requirements=plant_data["light_requirements"],
                                speed_to_growth=plant_data["speed_to_growth"],
                                fertilizer_required=plant_data["fertilizer_required"],
                                health=plant_data["health"]
                            )
                        else:
                            plant = Plant(plant_name)

                        plant.maturity = Maturity[plant_data["maturity"]]
                        plant.water = plant_data["water"]
                        plant.light = plant_data["light"]
                        plant.speed = plant_data["speed"]
                        plant.size = plant_data["size"]
                        plant.fertilizer = plant_data["fertilizer"]
                        plant.cut = plant_data["cut"]
                        plant.FinaleState = FinaleState[plant_data["FinaleState"]]
                        plant.day = plant_data["day"]

                        self.garden.plants.append(plant)

                    print(f"Game loaded successfully for {self.name_player}!")
                    return True

                except (FileNotFoundError, json.JSONDecodeError, KeyError) as e:
                    print(f"Error loading the save file: {e}. Starting a new game.")

        return False