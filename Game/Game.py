import Utils
from Garden import Garden
from Utils import choose_action
from Events.Event import Event
from Plants.Plant import Plant
from Plants.Tree import AppleTree
from Plants.Flower import Flower
from Plants.Enum_Plant import CREATE_PLANTS

class Game:
    def __init__(self, name_player:str) -> None:
        self.name_player = name_player
        self.garden: Garden | None = None
        self.action = 4
        self.money = 0
        self.seeds = {}

    def display_garden(self) -> None:
        print("\n\nHere is your garden now:\n")
        for plant in self.garden.plants:
            print(plant.__str__())
            print("---------------------------")

    def start(self, NUMBER_OF_PLANTS) -> None:
        list_temp = utils.choose_plants_to_beginning(NUMBER_OF_PLANTS)
        self.garden = Garden(list_temp)

    def sell_seed(self) -> None:
        seed_list = list(self.seeds.items())
        for index, (seed, quantity) in enumerate(seed_list, start=1):
            print(f"{index}. {seed}: {quantity} seeds")

            print("\nEnter the number of the seed type you want to sell: ")
            choice:int = utils.get_valid_number(len(seed_list))
            seed_name = seed_list[choice - 1][0]
            self.seeds[seed_name] -= 1
            print(f"You sold 1 {seed_name} seed.")
            self.money += 10
            print(f"You have now {self.money} money.")
            if self.seeds[seed_name] == 0:
                del self.seeds[seed_name]
                print(f"You no longer have any {seed_name} seeds.")

    def display_seeds(self) -> None:
        print("\nWhich plant seeds you want to sell ?")
        if len(self.seeds) == 0:
            print("You don't have any seeds yet.")
        else:
            print("\n\nHere is your seeds:\n")
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
        if plant.health - intensity < 0:
            plant.health = 0
        else:
            plant.health -= intensity

    def event(self, event: Event) -> None:
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
        nbr_plant_alive = 0
        for plant in self.garden.plants:
            if plant.check_is_dead():
                pass
            else:
                nbr_plant_alive += 1
        return nbr_plant_alive < 0

    def use_action(self):
        if self.check_action():
            self.action -=1
            print(f"You have left {self.action} action today !")
        else:
            self.add_day()
            print(f"This is a new day !")
            self.action = 4

    def check_action(self) -> bool:
        return self.action > 1

    def buy_plant(self):
        print("\nWhich plant plant you want to buy?")
        for plant in CREATE_PLANTS:
            print(f"{plant.name}")
        result = utils.get_valid_number(len(CREATE_PLANTS))
        if result == 1:
            self.garden + AppleTree(5, 7, 4, 0.07, 150)
        elif result == 2:
            self.garden + Flower(5, 10, 5, 0.2, 50, "blue")



    def choose_action(self) -> None:
        action = utils.choose_action()

        if action == 1:
            print("\nGive water to which plant ?")
            self.garden.get_name_plants()
            result = utils.get_valid_number(len(self.garden.plants))
            selected_plant = self.garden.plants[result - 1]
            print(selected_plant.__str__())
            nbr_water = utils.get_valid_number(10)
            selected_plant.give_water(nbr_water)
            self.use_action()
        elif action == 2:
            print("\nChange light to which plant ?")
            self.garden.get_name_plants()
            result = utils.get_valid_number(len(self.garden.plants))
            selected_plant = self.garden.plants[result - 1]
            print(selected_plant.__str__())
            nbr_light = utils.get_valid_number(10)
            selected_plant.change_light(nbr_light)
            self.use_action()
        elif action == 3:
            print("\nAdd fertilizer to which plant ?")
            self.garden.get_name_plants()
            result = utils.get_valid_number(len(self.garden.plants))
            selected_plant = self.garden.plants[result - 1]
            print(selected_plant.__str__())
            fertilizer = utils.get_valid_number(10)
            selected_plant.add_fertilizer(fertilizer)
            self.use_action()
        elif action == 4:
            print("\nwhich plant do you want to cut ?")
            self.garden.get_name_plants()
            result = utils.get_valid_number(len(self.garden.plants))
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
