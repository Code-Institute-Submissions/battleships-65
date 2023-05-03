"""
Battleships
How the game works:
1. The player chooses a 5x5, 8x8 or 10x10 grid
2. Each grid has 5 battleships placed at random
3. The player choose a row and column to choose to shoot
4. For every shot that hits or misses this will be displayed in the grid
5. If the player finds all the computer's ships first the players wins

Legend:
1. "-" = Water or empty space
2. "#" = Water that was shot with a bullet, a miss as no ship was hit
3. "*" = Ship that was hit
4. "@" = Position of player ships
"""
import random

game_board = []
board_size = 0
scores = {"player1": 0, "player2": 0}
player_one_name = ""
player_two_name = ""
game_state = "NAME_CHOICE"
player_one_board = []
player_two_board = []
letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}


def main():
    """
    This function uses a while loop
    to change between the menu and game
    """
    while game_state == "NAME_CHOICE":
        play_game()
    while game_state == "PLAY_GAME":
        display_board(game_board)


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

    def add_ships(self, x, y):
        self.ships.append((x, y))
        if self.type == "player":
            self.board[x][y] = "@"

    def make_guess(self, x, y):
        self.guesses.append((x, y))
        self.board[x][y] = "#"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Hit"
        else:
            return "Miss"


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
        game_board.board.append("-" * board_size)
    letter = 0
    for row in range(board_size):
        print(chr(letter + 65), end=" |")
        for column in range(len(game_board.board[letter])):
            print(game_board.board[letter][column], end=" ")
        letter += 1
        print("| ")


def generate_ships(board):
    """
    This function assigns the position of
    Computer and Player ships
    """
    # if board_size == 5:
    #     for num_ships in range(5):
    #         x, y = random.randint(0, 4), random.randint(0, 4)
    #         while board[x][y] == "*":
    #             x, y = random.randint(0, 4), random.randint(0, 4)
    #         board[x][y] = "*"
    # elif board_size == 8:
    #     for num_ships in range(5):
    #         x, y = random.randint(0, 7), random.randint(0, 7)
    #         while board[x][y] == "*":
    #             x, y = random.randint(0, 7), random.randint(0, 7)
    #         board[x][y] = "*"
    # elif board_size == 10:
    #     for num_ships in range(5):
    #         x, y = random.randint(0, 9), random.randint(0, 9)
    #         while board[x][y] == "*":
    #             x, y = random.randint(0, 9), random.randint(0, 9)
    #         board[x][y] = "*"
    # else:
    #     print("Error")
    if board_size == 5:
        x, y = random.randint(0, 4), random.randint(0, 4)
        board.add_ships(x, y)
    elif board_size == 8:
        x, y = random.randint(0, 7), random.randint(0, 7)
        board.add_ships(x, y)
    elif board_size == 10:
        x, y = random.randint(0, 9), random.randint(0, 9)
        board.add_ships(x, y)
    else:
        print("Error")
    # display_board(computer_board)
    # display_board(player_board)
    # make_guess()


def make_guess():
    """
    This function prompts the user to input a guess
    The player must choose a number and a letter
    """
    print("Please make a row choice")
    row_guess = input("Your row choice (letter): ").upper()
    # Include a try and except here in case user enters no data
    while row_guess not in "ABCDEFGHI":
        print("Please enter a valid row")
        row_guess = input("Your row choice (letter): ").upper()
    print("Please make a column choice")
    column_guess = input("Your column guess (number): ")
    while column_guess not in "123456789":
        print("Please enter a valid column")
        column_guess = input("Your column guess (number): ")
    # x = int(row_guess) - 1
    # y = letters_to_numbers[column_guess]
    # game_board.board.make_guess(x, y)
    # return x, y
    return letters_to_numbers[row_guess], int(column_guess) - 1


def count_hit_ships(board):
    count = 0
    for row in board:
        for col in row:
            if col == "*":
                count += 1
    return count


def new_game():
    """
    This function sets the number of ships to 5
    Calls the board class to assign the required variables
    to both the player and computer boards
    """
    size = board_size
    num_ships = 5
    computer_board = Board(size, num_ships, "Computer", type="computer")
    player_board = Board(size, num_ships, player_name, type="player")
    for _ in range(num_ships):
        generate_ships(player_board)
        generate_ships(computer_board)
    display_board(player_board)
    display_board(computer_board)
    # make_guess()
    turns = 0
    while True:
        # guess_row = int(input("Guess Row: "))
        # guess_col = int(input("Guess Column: "))
        guess_row, guess_col = make_guess()
        if computer_board.board[guess_row][guess_col] != "-":
            print("Hit")
            computer_board.board[guess_row][guess_col] = "#"
            turns += 1
            num_ships -= 1
            ship_sunk = True
            for row in computer_board.board:
                if ship_sunk and computer_board.board[guess_row][guess_col] in row:
                    ship_sunk = False
                    break
                if ship_sunk:
                    print("You have sunk a ship")
        else:
            print("Miss")
            computer_board.board[guess_row][guess_col] = "O"
            turns += 1
        display_board(player_board)
        display_board(computer_board)
        if num_ships == 0:
            print(f"Congratulations, you have sunk all ships in {turns} turns")
            break
        elif turns == 10:
            print("Game Over. You have used all your turns")
            break


def play_game():
    """
    This function prints a welcome message and
    ASCII Art is used to display a Battleship
    Requests input from the user for name and
    for the user to choose a grid size
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
    global player_name
    player_name = input("Please enter your name: \n")
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
                global game_state
                game_state = "PLAY_GAME"
    except ValueError as e:
        print(f"{e} This choice is invalid. Please try again\n")


play_game()
main()
