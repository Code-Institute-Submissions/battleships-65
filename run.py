game_board = []
board_size = 0
scores = {"computer": 0, "player": 0}
computer_board = []
player_board = []


class Board:
    """
    Sets the number of ships, the name and
    whether it is the computer or player board type
    The class has methods for adding ships and guesses
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["-" for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"

    def add_ships(self, x, y):
        self.ships.append((x, y))
        if self.type == "player":
            self.board[x][y] = "@"


def display_board(game_board):
    """
    This function displays the game board
    The amount of numbers and letters displayed,
    depend on the grid size chosen by the player
    """
    number_line = "   "
    for index in range(board_size):
        number_line += f"{index+1} "
    print(number_line)
    for row in range(board_size):
        game_board.append("-" * board_size)
    letter = 0
    for row in range(board_size):
        print(chr(letter + 65), end=" |")
        for column in range(len(game_board[letter])):
            print(game_board[letter][column], end=" ")
        letter += 1
        print("| ")


def populate_board(board):
    """
    This function assigns the position of
    Computer and Player ships
    """
    display_board(computer_board)
    display_board(player_board)
    for x in range(board_size):
        for y in range(board_size):
            board.add_ships(x, y)

    make_guess()


def make_guess():
    print("Please make a choice")
    print("Your choice must be a combination of a number and a letter")
    player_guess = input("Your choice: ")
    print(f"You have chosen {player_guess}")


def new_game():
    """
    This function sets the number of ships to 5
    Calls the board class to assign the required variables
    to both the player and computer boards
    """
    size = board_size
    num_ships = 5
    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, "Player", type="player")
    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)


def main():
    """
    This function prints a welcome message
    Requests input from the user for name
    Requests for the user to choose a grid size
    """
    print("Welcome to Battleships\n")
    print("                           |-._")
    print("                           |-._|")
    print("                           |")
    print("                       ___#|#___")
    print("                 __  |____________|  __")
    print("             <=====| | |        | | |====>")
    print("       <=====| |.----------------------. | |====>")
    print("\\-------------' .  .  .  .  .  .  .  .  . '--------------//")
    print(" \\                                                      //")
    print("  \\_______________________________________LE___________//")
    print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    print("wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww")
    input("Please enter your name: \n")
    print("Please choose which grid you wish to play on\n")
    print("Grid sizes are 5, 8 or 10\n")
    user_choice = int(input("Grid size choice: "))
    validate_grid_size(user_choice)


def validate_grid_size(choice):
    """
    This function validates the user's grid choice
    If the user chooses a value that is not 5, 8 or 10
    The user is requested to provide a valid choice
    If the user chooses a valid choice
    They are asked to confirm their choice and the game begins
    """
    try:
        if choice not in [5, 8, 10]:
            print(f"Choice of {choice} is invalid, please choose a valid choice\n")
        else:
            confirm = input(f"please confirm choice of {choice}, press Y to confirm ")
            if confirm in ["y", "Y", "Yes", "YES", "yes"]:
                global board_size
                board_size = int(choice)
                print("Thank you, the game will now commence")
                new_game()
            else:
                main()
    except ValueError as e:
        print(f"{e} This choice is invalid. Please try again\n")


main()
