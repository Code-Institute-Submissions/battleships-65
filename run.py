game_board = []
board_size = 0


def main():
    print("Welcome to Battleships\n")
    print("                           |-._")
    print("                           |-._|")
    print("                           |")
    print("                       ___#|#___")
    print("                 __  |____________|  __")
    print("             <=====| | |        | | |====>")
    print("       <=====| |.----------------------. | |====>")
    print("\-------------' .  .  .  .  .  .  .  .  . '--------------/")
    print(" \                                                      /")
    print("  \_______________________________________LE___________/")
    print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
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
                global board_size
                board_size = int(choice)
                print("Thank you, the game will now commence")
                display_board(game_board)
            else:
                main()
    except ValueError as e:
        print(f"{e} This choice is invalid. Please try again\n")


def display_board(game_board):
    print("   1 2 3 4 5 6 7 8 9 10")
    for row in range(board_size):
        game_board.append("-" * board_size)
    letter = 0
    for row in range(board_size):
        print(chr(letter + 65), end=" |")
        for column in range(len(game_board[letter])):
            print(game_board[letter][column], end=" ")
        letter += 1
        print("| ")


main()
