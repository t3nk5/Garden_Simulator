import random
from Utils import *
from Game.Game import Game
from Events.Event import Event


NUMBER_OF_PLANTS = 2

def main():
    """
        Main function to run the garden game. This function handles the game loop where the user is prompted to interact
        with the game, including choosing actions for their garden, and receiving random events.
        - Greets the user and asks for their name.
        - Initializes the game with the player’s name and starts a new game or loads a previous game.
        - Continuously displays the garden's status and asks the player to choose an action.
        - Random events (with a 10% probability) occur during the game.
        - Checks if the game is finished after each action and event.
    """
    print("Welcome to the Garden Game!\n")

    player_name = input("Enter your name: ").strip()
    game = Game(player_name)

    if not game.load_game():
        print("Starting a new game...")
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

        if game.is_finished():
            finish = True

if __name__ == "__main__":
    main()

