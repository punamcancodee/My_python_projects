import pygame
from dimension import *
class Game:
    def __init__(self):
        pass

# showing the methods for rendering our chess board
#''' here the surface we used is meant to be working with self.screen from main '''
    def show_bg(self , surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row+col) % 2== 0:
                    color = (234, 235 , 200) # this refers to the light green
                else:
                    color= (119,154,88) # this refers to the dark green
                rect = (col * SQSIZE, row * SQSIZE , SQSIZE , SQSIZE)
                pygame.draw.rect(surface,color,rect)
