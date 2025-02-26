from test import test
from utils import *
from Game.Game import Game


NUMBER_OF_PLANTS = 2

def main():

    player_name = input("Enter your name: ")
    game = Game(player_name)

    game.start(NUMBER_OF_PLANTS)
    game.display_garden()

    game.choose_action()
    game.display_garden()








if __name__ == "__main__":
    main()

