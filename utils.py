from Plants.Tree import *
from Plants.Flower import *
from Plants.Enum_Plant import CREATE_PLANTS

def get_valid_number(max_value) -> int:
    while True:
        try:
            user_input = int(input(f"Enter a number between 0 and {max_value}: "))
            if 0 < user_input <= max_value :
                return user_input
            else:
                print(f"The number must be between 0 and {max_value}. Try again.")
        except ValueError:
            print("Invalid entry. Please enter a whole number.")


def choose_plants_to_beginning(number_of_plants: int) -> list:
    print("\nStart to cultivate your garden ;)")
    chosen_plants = []

    for i in range(number_of_plants):
        print(f"\nChoose the type of your plant {i + 1} :")
        for plant in CREATE_PLANTS:
            print(f"{plant.value} → {plant.name.capitalize()}")

        plant_choice = get_valid_number(len(CREATE_PLANTS))

        if CREATE_PLANTS(plant_choice) == CREATE_PLANTS.TREE:
            chosen_plants.append(AppleTree(5, 7, 4, 0.07, 150))
        elif CREATE_PLANTS(plant_choice) == CREATE_PLANTS.FLOWER:
            chosen_plants.append(Flower(5, 10, 5, 0.2, 50, "red"))

    return chosen_plants