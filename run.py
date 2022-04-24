from random import randint
import os

class Colors:
    """
    This class defines basic color pallette used in the game.
    """
    RED = '\033[91m'
    VIOLET = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'    
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Welcome message
print('*' * 60)
print('')
print("Welcome to:")
print(
    f"""{Colors.VIOLET}{Colors.BOLD}
     _______   _    _   _   _____   _______  __    __
    |__   __| | |  | | | | |  __ \ |__   __| \ \  / /
       | |    | |__| | | | | |__| |   | |     \ \/ /
       | |    |  __  | | | |  __ /    | |      \  /
       | |    | |  | | | | | |\ \     | |      |  | 
       |_|    |_|  |_| |_| |_| \_\    |_|      |__|
       ______   _    _   ______   _______   ______
      /    __\ | |  | | |  __  | |__   __| /    __/
      |   (    | |__| | | |  | |    | |    \   (
       \   \   |  __  | | |  | |    | |     \   \.
     ___)   \  | |  | | | |__| |    | |   ___)   \.
    \_______/  |_|  |_| |______|    |_|  \_______/
{Colors.WHITE}"""
)
print('*' * 60)
print('')

user_name = input("What is your name?\n")
os.system('cls||clear')
print(f"\n{Colors.GREEN}You look like a brave soldier {user_name}{Colors.WHITE}")

USER_INSTRUCTIONS = f"""\nThis is your mission:
You must defend Oros harbour from our enemy Chatarra.
Oros is much coveted for the precious golden mineral covering our cliffs.
Our watchmen have spotted the enemy's fleet fast approaching.
You will have to destroy their 4 ships before they land.
If you do not succeed, they will steal our gold.
You only have 30 cannonballs to complete your mission.
Do not run out of ammunition or Chatarra's troops will make it ashore.

{Colors.GREEN}The fate of Oros harbour is in your hands...{Colors.WHITE}

One more thing:
If a ship is hit, it will be marked as 'X'
If it's a miss, it will be marked as '-'.
"""

print(USER_INSTRUCTIONS)

# Code credit on Ship class goes to Cloud2236863496
# https://discuss.codecademy.com/u/cloud2236863496/summary


class Ship:

    def __init__(self, size, orientation, location):
        '''
        Function to define size, orientation and location of ships
        '''
        self.size = size

        if orientation == 'horizontal' or orientation == 'vertical':
            self.orientation = orientation
        else:
            raise ValueError("Value must be 'horizontal' or 'vertical'.")

        if orientation == 'horizontal':
            if location['row'] in range(ROW_SIZE):
                self.coordinates = []
                for index in range(size):
                    if location['col'] + index in range(COL_SIZE):
                        self.coordinates.append({
                            'row': location['row'],
                            'col': location['col'] +
                            index})
                    else:
                        raise IndexError("Column is out of range.")
            else:
                raise IndexError("Row is out of range.")
        elif orientation == 'vertical':
            if location['col'] in range(COL_SIZE):
                self.coordinates = []
                for index in range(size):
                    if location['row'] + index in range(ROW_SIZE):
                        self.coordinates.append({
                            'row': location['row'] + index,
                            'col': location['col']})
                    else:
                        raise IndexError("Row is out of range.")
            else:
                raise IndexError("Column is out of range.")

        if self.filled():
            print_board(board)
            print(" ".join(str(coords) for coords in self.coordinates))
            raise IndexError("A ship already occupies that space.")
        else:
            self.fill_board()

    def filled(self):
        '''
        Function to chek if a ship already occupies a space on board
        '''
        for coords in self.coordinates:
            if board[coords['row']][coords['col']] == 1:
                return True
        return False

    def fill_board(self):
        '''
        Function to fill a space on board
        '''
        for coords in self.coordinates:
            board[coords['row']][coords['col']] = 1

    def contains(self, location):
        '''
        Function to check if the location does contain a ship on board
        '''
        for coords in self.coordinates:
            if coords == location:
                return True
        return False

    def destroyed(self):
        '''
        Function to check if ship destroyed on user's board
        '''
        for coords in self.coordinates:
            if board_display[coords['row']][coords['col']] == 'O':
                return False
            elif board_display[coords['row']][coords['col']] == '-':
                raise RuntimeError("Board display inaccurate")
        return True


# Settings Variables
ROW_SIZE = 7
COL_SIZE = 7
NUM_SHIPS = 4
MAX_SHIP_SIZE = 5
MIN_SHIP_SIZE = 2
NUM_TURNS = 30

# Create lists
ship_list = []

board = [[0] * COL_SIZE for x in range(ROW_SIZE)]

board_display = [["O"] * COL_SIZE for x in range(ROW_SIZE)]

# All Other Functions


def print_board(board_array):
    '''
    Function to print board
    '''
    print("\n  " + " ".join(str(x) for x in range(1, COL_SIZE + 1)))
    for row in range(ROW_SIZE):
        print(str(row + 1) + " " + " ".join(str(column)
              for column in board_array[row]))
    print()


def search_locations(size, orientation):
    '''
    Function to searh for locations based on size and orientation constraints
    including if statements to remain within range of board
    '''
    locations = []

    if orientation != 'horizontal' and orientation != 'vertical':
        raise ValueError("Orientation must be 'horizontal' or 'vertical'.")

    if orientation == 'horizontal':
        if size <= COL_SIZE:
            for row in range(ROW_SIZE):
                for column in range(COL_SIZE - size + 1):
                    if 1 not in board[row][column:column+size]:
                        locations.append({'row': row, 'col': column})
    elif orientation == 'vertical':
        if size <= ROW_SIZE:
            for column in range(COL_SIZE):
                for row in range(ROW_SIZE - size + 1):
                    if 1 not in [board[i][column]
                                 for i in range(row, row+size)]:
                        locations.append({'row': row, 'col': column})

    if not locations:
        return 'None'
    else:
        return locations


def random_location():
    '''
    Function to generate a random ship location
    '''
    size = randint(MIN_SHIP_SIZE, MAX_SHIP_SIZE)
    orientation = 'horizontal' if randint(0, 1) == 0 else 'vertical'

    locations = search_locations(size, orientation)
    if locations == 'None':
        return 'None'
    else:
        return {'location': locations[randint(0, len(locations) - 1)],
                'size': size, 'orientation': orientation}


def get_row():
    '''
    Function to facilitate input of row guess and print an error message
    if out of scope
    '''
    while True:
        try:
            guess = int(input("Row Guess:\n"))
            if guess in range(1, ROW_SIZE + 1):
                return guess - 1
            else:
                print("\nNo way, that was such a wild guess :P")
        except ValueError:
            print("\nPlease enter a valid number")


def get_col():
    '''
    Function to facilitate input of column guess and print
    an error message if out of scope
    '''
    while True:
        try:
            guess = int(input("Column Guess:\n"))
            if guess in range(1, COL_SIZE + 1):
                return guess - 1
            else:
                print("\nNo way, that was such a wild guess :P")
        except ValueError:
            print("\nPlease enter a valid number")


# Create the ships
TEMP = 0
while TEMP < NUM_SHIPS:
    ship_char = random_location()
    if ship_char == 'None':
        continue
    else:
        ship_list.append(Ship(ship_char['size'], ship_char['orientation'],
                         ship_char['location']))
        TEMP += 1
del TEMP

# Play Game (including print number of ships left, print if hit
# or miss and print if one ship is fully sunk)


answer = input(f"{Colors.GREEN}Do you accept the mission? (yes/no){Colors.WHITE}\n")

if answer.lower().strip() == "no":
    os.system('cls||clear')
    print(f"{Colors.YELLOW}Too bad {user_name}, we could have done with a brave soldier :-/{Colors.WHITE}")
    quit()
else:
    os.system('clear')
    print(f"{Colors.GREEN}That is great news, thank you for your help soldier {user_name}{Colors.WHITE}\n")
    print_board(board_display)

    for turn in range(NUM_TURNS):
        print(f"{Colors.BLUE}Turn:", turn + 1, "of", NUM_TURNS)
        print(f"{Colors.YELLOW}Ships left:", len(ship_list))
        print(f"{Colors.RED}Get ready to fire!{Colors.WHITE}")
        print()

        guess_coords = {}
        while True:
            guess_coords['row'] = get_row()
            guess_coords['col'] = get_col()
            if (
                board_display[guess_coords['row']]
                [guess_coords['col']] == 'X' or
                board_display[guess_coords['row']][guess_coords['col']] == '-'
            ):
                print("\nYou guessed that one already.")
            else:
                break

        os.system('clear')

        SHIP_HIT = False
        for ship in ship_list:
            if ship.contains(guess_coords):
                print("Hit!")
                SHIP_HIT = True
                board_display[guess_coords['row']][guess_coords['col']] = 'X'
                if ship.destroyed():
                    print("You sunk a ship!")
                    ship_list.remove(ship)
                break
        if not SHIP_HIT:
            board_display[guess_coords['row']][guess_coords['col']] = '-'
            print("You missed...")

        print_board(board_display)

        if not ship_list:
            break

# End Game (including print if users wins when there are no more ships to sink
# or print if user loses if ships are still left)
if ship_list:
    print(f"Oh no...you have failed this time soldier {user_name}")
    print("")
    print("""It looks like Chatarra's troups will steal our gold.
You can always press on 'Run Program' to try again"""
)
          
else:
    print(f"Mission accomplished {user_name}!")
    print("")
    print("""You managed to sink all of the enemy's ships
and you saved our gold!""")
