from random import randint
import os

# Ship Class
class Ship
    ''' 
    Function to define size, orientation and location of user's ships
    '''
    def __init__(self, size, orientation, location):
        self.size = size
    
        if orientation == 'horizontal' or orientation == 'vertical':
            self.orientation = orientation
        else:
            raise ValueError("Value must be 'horizontal' or 'vertical'.")

            if orientation == 'horizontal':
                if location['row'] in range(row_size):
                    self.coordinates = []
                    for index in range(size):
                        if location['col'] + index in range(col_size):
                            self.coordinates.append({'row': location['row'], 'col': location['col'] + index})
                        else:
                            raise IndexError("Column is out of range.")
                else:
                    raise IndexError("Row is out of range.")
            elif orientation == 'vertical':
                if location['col'] in range(col_size):
                    self.coordinates = []
                    for index in range(size):
                        if location['row'] + index in range(row_size):
                            self.coordinates.append({'row': location['row'] + index, 'col': location['col']})
                        else:
                            raise IndexError("Row is out of range.")
                else:
                    raise IndexError("Column is out of range.")

            if self.filled():
                print_board(board)
                print(" ".join(str(coords) for coords in self.coordinates))
                raise IndexError("A ship already occupies that space.")
            else:
                self.fillBoard()

    ''' 
    Function to chek if a ship already occupies a space on user's board
    '''
    def filled(self):
        for coords in self.coordinates:
            if board[coords['row']][coords['col']] == 1:
                return True
        return False

    ''' 
    Function to fill a space on user's board
    '''
    def fillBoard(self):
        for coords in self.coordinates:
        board[coords['row']][coords['col']] = 1

    ''' 
    Function to check if the location does contain a ship on the user's board
    '''
    def contains(self, location):
        for coords in self.coordinates:
            if coords == location:
                return True
        return False

    ''' 
    Function to check if ship destroyed on user's board
    '''
    def destroyed(self):
        for coords in self.coordinates:
            if board_display[coords['row']][coords['col']] == 'O':
                return False
            elif board_display[coords['row']][coords['col']] == '*':
                raise RuntimeError("Board display inaccurate")
        return True

#Settings Variables
row_size = 8 #number of rows
col_size = 8 #number of columns
num_ships = 4
max_ship_size = 5
min_ship_size = 2
num_turns = 30

#Create lists
ship_list = []

board = [[0] * col_size for x in range(row_size)]

board_display = [[" "] * col_size for x in range(row_size)]

#All Other Functions

''' 
Function to print board
'''
def print_board(board_array):
  print("\n  " + " ".join(str(x) for x in range(1, col_size + 1)))
  for r in range(row_size):
    print(str(r + 1) + " " + " ".join(str(c) for c in board_array[r]))
  print()

'''
Function to searh for locations based on size and orientation constraints including if statements to remain within range of board 
'''
def search_locations(size, orientation):
    locations = []

    if orientation != 'horizontal' and orientation != 'vertical':
        raise ValueError("Orientation must have a value of either 'horizontal' or 'vertical'.")

    if orientation == 'horizontal':
        if size <= col_size:
            for r in range(row_size):
                for c in range(col_size - size + 1):
                    if 1 not in board[r][c:c+size]:
                        locations.append({'row': r, 'col': c})
    elif orientation == 'vertical':
        if size <= row_size:
            for c in range(col_size):
                for r in range(row_size - size + 1):
                    if 1 not in [board[i][c] for i in range(r, r+size)]:
                        locations.append({'row': r, 'col': c})

    if not locations:
        return 'None'
    else:
        return locations

''' 
Function to generate a random ship location
'''
def random_location():
    size = randint(min_ship_size, max_ship_size)
    orientation = 'horizontal' if randint(0, 1) == 0 else 'vertical'

    locations = search_locations(size, orientation)
    if locations == 'None':
        return 'None'
    else:
        return {'location': locations[randint(0, len(locations) - 1)], 'size': size,\
            'orientation': orientation}

''' 
Function to facilitate input of row guess and print an error message if out of scope
'''
def get_row():
    while True:
        try:
            guess = int(input("Row Guess: "))
            if guess in range(1, row_size + 1):
                return guess - 1
            else:
                print("\no way, that was a loong shot!")
        except ValueError:
            print("\nPlease enter a number")

