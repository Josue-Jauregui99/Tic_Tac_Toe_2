import math
import random
import pygame as pg
from src import constants

class GameplayView:
    template_name = 'gameplay.html'

    def __init__(self):
        pass

    def draw_board(self, screen, board, sectors):
        screen.fill(constants.BLACK)
        #Board
        R = int((math.sin(pg.time.get_ticks()/1000)**2)*255)
        G = int((math.cos(pg.time.get_ticks()/1000)**2)*255)
        B = int(((math.sin(pg.time.get_ticks()/2000))**2)*255)
        alpha = random.randint(50,100)/100
        board_color = (R, G, B,alpha)
        #Vertical Lines
        pg.draw.line(screen,board_color,(constants.MIN_BOARD_WIDTH+constants.DISTANCE_VERTICAL, constants.MIN_BOARD_HEIGHT),(constants.MIN_BOARD_WIDTH+constants.DISTANCE_VERTICAL,constants.MAX_BOARD_HEIGHT),5)
        pg.draw.line(screen,board_color,(constants.MAX_BOARD_WIDTH-constants.DISTANCE_VERTICAL, constants.MIN_BOARD_HEIGHT),(constants.MAX_BOARD_WIDTH-constants.DISTANCE_VERTICAL,constants.MAX_BOARD_HEIGHT),5)
        #Horizontal Lines
        pg.draw.line(screen,board_color,(constants.MIN_BOARD_WIDTH,constants.MIN_BOARD_HEIGHT+constants.DISTANCE_HORIZONTAL),(constants.MAX_BOARD_WIDTH,constants.MIN_BOARD_HEIGHT+constants.DISTANCE_HORIZONTAL),5)
        pg.draw.line(screen,board_color,(constants.MIN_BOARD_WIDTH,constants.MAX_BOARD_HEIGHT - constants.DISTANCE_HORIZONTAL),(constants.MAX_BOARD_WIDTH,constants.MAX_BOARD_HEIGHT - constants.DISTANCE_HORIZONTAL),5)

        for n in range(9):
            if board[n] != '':
                screen.blit(pg.font.SysFont('Arial', 50).render(board[n], True, (255, 255, 255)), (sectors[n].centerx-15, sectors[n].centery-30))

