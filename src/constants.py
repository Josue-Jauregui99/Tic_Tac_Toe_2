import pygame as pg


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
DISTANCE = 5
MAX_BOARD_WIDTH = SCREEN_WIDTH/5*4
MIN_BOARD_WIDTH = SCREEN_WIDTH/5
MAX_BOARD_HEIGHT = (SCREEN_HEIGHT/3*2)-5
MIN_BOARD_HEIGHT = 5
DISTANCE_VERTICAL = (MAX_BOARD_WIDTH-MIN_BOARD_WIDTH)/3
DISTANCE_HORIZONTAL = (MAX_BOARD_HEIGHT-MIN_BOARD_HEIGHT)/3

#Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
CYAN = (0, 255, 255)

MAIN_MENU_OPTIONS = ["Single", "Multiplayer", "Settings", "High Scores", "Credits", "Quit"]

