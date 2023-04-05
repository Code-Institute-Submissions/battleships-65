def main():
    print("Welcome to Battleships\n")
    input("Please enter your name: \n")
    print("Please choose which grid you wish to play on\n")
    print("Grid sizes are 5, 8 or 10\n")
    user_choice = int(input("Grid size choice: "))
    validate_grid_size(user_choice)


def validate_grid_size(choice):
    try:
        if choice not in [5, 8, 10]:
            print(f"Choice of {choice} is invalid, please choose a valid choice\n")
        else:
            confirm = input(f"please confirm choice of {choice}, press Y to confirm ")
            if confirm in ["y", "Y", "Yes", "YES", "yes"]:
                print("Thank you, the game will now commence")
                # game logic
            else:
                main()
    except ValueError as e:
        print(f"{e} This choice is invalid. Please try again\n")


main()
