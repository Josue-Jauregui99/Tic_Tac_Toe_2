from src import constants
from src.main_menu_loop import MainMenuLoop

import pygame as pg


def main():
    pg.init()
    
    running = True
    screen = pg.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pg.display.set_caption("Tic Tac Toe")
    main_menu = MainMenuLoop(screen)
    pg.quit()


if __name__ == '__main__':
    main()