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



    def contains(self, location):
    def destroyed(self):

