
## if this module is not initilly installed on your pc you can simply use python -m  pip install pygame,and similary others as per the need ##
''' pygame is the module in python usually used to develop 2d games  and sys is used to manipulte different functions and variables to work in runtime environment'''

import pygame
import sys

from dimension import *
from game_play import Game


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(  (WIDTH, HEIGHT)  )
        pygame.display.set_caption('chess')
        self.game = Game()

    def mainloop(self):
        screen = self.screen
        game = self.game
        while True :

            self.game.show_bg(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                    

            pygame.display.update()



main = Main()
main.mainloop()
