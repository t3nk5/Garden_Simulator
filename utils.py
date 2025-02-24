

def get_valid_number(max_value) -> int:
    while True:
        try:
            user_input = int(input(f"Enter a number between 0 and {max_value -1}: "))
            if 0 <= user_input <= max_value - 1:
                return user_input
            else:
                print(f"❌ The number must be between 0 and {max_value}. Try again.")
        except ValueError:
            print("❌ Invalid entry. Please enter a whole number.")