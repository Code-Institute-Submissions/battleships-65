def main():
    print("Welcome to Battleships\n")
    input("Please enter your name: \n")
    print("Please choose which grid you wish to play on\n")
    print("Grid sizes are 5, 8 or 10\n")
    user_choice = int(input("Grid size choice:"))
    validate_grid_size(user_choice)

def validate_grid_size(choice):
    try:
        if choice != 5 or 8 or 10:
            raise ValueError(f"Error. You chose {choice} Only values of 5, 8 and 10 are accepted\n")
    except ValueError as e:
        print(f"You have chosen {choice}. This is invalid. Please try again\n")

main()