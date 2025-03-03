from Plants.Salad import Salad
from Plants.Tree import *
from Plants.Flower import *
from Plants.Enum_Plant import CREATE_PLANTS

def get_valid_number(max_value :int) -> int:
    """
        Prompts the user to input a valid number within a specified range.
        Args:
            max_value (int): The maximum valid number that the user can input.
        Returns:
            int: A valid number between 1 and max_value (inclusive).
        Raises:
            ValueError: If the user input is not a valid integer or is out of range.
        """
    while True:
        try:
            user_input = int(input(f"Enter a number between 1 and {max_value }: "))
            if 0 < user_input <= max_value :
                return user_input
            else:
                print(f"The number must be between 1 and {max_value }. Try again.")
        except ValueError:
            print("Invalid entry. Please enter a whole number.")

def choose_plants_to_beginning(number_of_plants: int) -> list:
    """
        Prompts the user to choose a specified number of plants to begin their garden.
        Args:
            number_of_plants (int): The number of plants the user wants to choose for their garden.
        Returns:
            list: A list of plant objects selected by the user.
    """
    print("\nStart to cultivate your garden ;)\nYou can choose 2 plants")
    chosen_plants = []

    for i in range(number_of_plants):
        print(f"\nChoose the type of your plant {i + 1} :")
        for plant in CREATE_PLANTS:
            print(f"{plant.value} → {plant.name.capitalize()}")

        plant_choice = get_valid_number(len(CREATE_PLANTS))

        if CREATE_PLANTS(plant_choice) == CREATE_PLANTS.TREE:
            chosen_plants.append(AppleTree(5, 7, 4, 0.3, 125))
        elif CREATE_PLANTS(plant_choice) == CREATE_PLANTS.FLOWER:
            chosen_plants.append(Flower(5, 10, 5, 0.1, 30, "red"))
        elif CREATE_PLANTS(plant_choice) == CREATE_PLANTS.SALAD:
            chosen_plants.append(Salad(7, 8, 3, 0.2, 50))

    return chosen_plants

def display_actions() -> None:
    """
        Displays a list of possible actions that the user can take in the garden game.
        This function does not take any parameters and does not return any values.
    """
    print("\nYou can:\n1-Give water\n2-Change the light\n3-Add fertilizer\n4-Cut\n5-Sell your inventory\n6-Buy a plant\n7-Save")

def choose_action() -> int:
    """
        Prompts the user to choose an action from a list of available actions in the garden game.
        Returns:
            int: The number corresponding to the chosen action (1 through 7).
    """
    print("\nChoose the type of your action :)")
    display_actions()
    action = get_valid_number(7)
    return action

