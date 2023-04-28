from dimension import *
from square_board import square


class Board:

    def __init__(self) :  
        self.squares = [[0,0,0,0,0,0,0,0] for col in range  (COLS)] 
        self.create()


    def _create(self):
      
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = square(row,col)

    def _add_pieces(self, color):
        pass