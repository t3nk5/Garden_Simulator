import utils
from Garden import Garden
from utils import choose_action
from Events.event import Event

class Game:
    def __init__(self, name_player:str) -> None:
        self.name_player = name_player
        self.garden = None

    def display_garden(self) -> None:
        print("\n\nHere is your garden now:\n")
        for plant in self.garden.plants:
            print(plant.__str__())
            print("---------------------------")

    def start(self, NUMBER_OF_PLANTS) -> None:
        list_temp = utils.choose_plants_to_beginning(NUMBER_OF_PLANTS)
        self.garden = Garden(list_temp)



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
        elif action == 2:
            print("\nChange light to which plant ?")
            self.garden.get_name_plants()
            result = utils.get_valid_number(len(self.garden.plants))
            selected_plant = self.garden.plants[result - 1]
            print(selected_plant.__str__())
            nbr_light = utils.get_valid_number(10)
            selected_plant.change_light(nbr_light)
        elif action == 3:
            print("\nAdd fertilizer to which plant ?")
            self.garden.get_name_plants()
            result = utils.get_valid_number(len(self.garden.plants))
            selected_plant = self.garden.plants[result - 1]
            print(selected_plant.__str__())
            fertilizer = utils.get_valid_number(10)
            selected_plant.add_fertilizer(fertilizer)
        elif action == 4:
            print("\nwhich plant do you want to cut ?")
            self.garden.get_name_plants()
            result = utils.get_valid_number(len(self.garden.plants))
            selected_plant = self.garden.plants[result - 1]
            print(selected_plant.__str__())
            if selected_plant.cut_plant():
                pass
            else: choose_action()


        elif action == 5:
            pass
        elif action == 6:
            pass



    def event(self, event: Event) -> None:
        intensity = event.intensity
        if event.event_type == event.event_type.STORM:
            for plant in self.garden.plants:
                plant.water += intensity
                plant.health -= intensity
        elif event.event_type == event.event_type.DROUGHT:
            for plant in self.garden.plants:
                plant.water -= intensity
                plant.health += intensity
        elif event.event_type == event.event_type.PARASITE:
            for plant in self.garden.plants:
                plant.health -= intensity * 2
        elif event.event_type == event.event_type.DISEASE:
            for plant in self.garden.plants:
                plant.health -= intensity

