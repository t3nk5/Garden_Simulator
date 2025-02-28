import random
from utils import *
from Game.Game import Game
from Events.event import Event


NUMBER_OF_PLANTS = 2

def main():

    player_name = input("Enter your name: ")
    game = Game(player_name)

    game.start(NUMBER_OF_PLANTS)

    finish = False
    while not finish:
        game.display_garden()
        game.choose_action()

        random_event = random.uniform(0.0, 1.0) < 0.1
        if random_event:
            event = Event()
            print(event.__str__())
            game.event(event)








if __name__ == "__main__":
    main()

