import utils

class Game:
    def __init__(self, name_player:str) -> None:
        self.name_player = name_player
        self.list_plant = None

    def display_garden(self) -> None:
        print("\n\nHere is your garden now:\n")
        for plant in self.list_plant:
            print(plant.__str__())
            print("---------------------------")

    def start(self, NUMBER_OF_PLANTS) -> None:
        self.list_plant= utils.choose_plants_to_beginning(NUMBER_OF_PLANTS)




    def choose_action(self, ) -> None:
        pass
