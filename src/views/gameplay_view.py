import math
import random
import pygame as pg
from src import constants
from src.components.button import Button

class GameplayView:
    template_name = 'gameplay.html'

    def __init__(self, screen):
        pg.font.init()
        button_font = pg.font.SysFont('Arial', 20)
        self.screen = screen
        self.continue_button = Button(constants.SCREEN_WIDTH//2-50, constants.SCREEN_HEIGHT//2+50, 100, 50, "Continue", button_font, constants.BLACK, constants.WHITE, constants.WHITE, constants.BLACK)
        self.quit_button = Button(constants.SCREEN_WIDTH//2-50, constants.SCREEN_HEIGHT//2+120, 100, 50, "Quit", button_font, constants.BLACK, constants.WHITE, constants.WHITE, constants.BLACK)

    def draw_board(self, board, sectors):
        self.screen.fill(constants.BLACK)
        #Board
        R = int((math.sin(pg.time.get_ticks()/1000)**2)*255)
        G = int((math.cos(pg.time.get_ticks()/1000)**2)*255)
        B = int(((math.sin(pg.time.get_ticks()/2000))**2)*255)
        alpha = random.randint(50,100)/100
        board_color = (R, G, B,alpha)
        #Vertical Lines
        pg.draw.line(self.screen,board_color,(constants.MIN_BOARD_WIDTH+constants.DISTANCE_VERTICAL, constants.MIN_BOARD_HEIGHT),(constants.MIN_BOARD_WIDTH+constants.DISTANCE_VERTICAL,constants.MAX_BOARD_HEIGHT),5)
        pg.draw.line(self.screen,board_color,(constants.MAX_BOARD_WIDTH-constants.DISTANCE_VERTICAL, constants.MIN_BOARD_HEIGHT),(constants.MAX_BOARD_WIDTH-constants.DISTANCE_VERTICAL,constants.MAX_BOARD_HEIGHT),5)
        #Horizontal Lines
        pg.draw.line(self.screen,board_color,(constants.MIN_BOARD_WIDTH,constants.MIN_BOARD_HEIGHT+constants.DISTANCE_HORIZONTAL),(constants.MAX_BOARD_WIDTH,constants.MIN_BOARD_HEIGHT+constants.DISTANCE_HORIZONTAL),5)
        pg.draw.line(self.screen,board_color,(constants.MIN_BOARD_WIDTH,constants.MAX_BOARD_HEIGHT - constants.DISTANCE_HORIZONTAL),(constants.MAX_BOARD_WIDTH,constants.MAX_BOARD_HEIGHT - constants.DISTANCE_HORIZONTAL),5)

        for n in range(9):
            if board[n] != '':
                self.screen.blit(pg.font.SysFont('Arial', 50).render(board[n], True, (255, 255, 255)), (sectors[n].centerx-15, sectors[n].centery-30))
    
    def game_over_screen(self, status, player):
        self.screen.fill(constants.BLACK)
        if status == 'winner':
            self.screen.blit(pg.font.SysFont('Arial', 50).render('Player ' + player + ' wins!', True, (255, 255, 255)), (constants.SCREEN_WIDTH//2-100, constants.SCREEN_HEIGHT//2-50))
        else:
            self.screen.blit(pg.font.SysFont('Arial', 50).render('It is a draw!', True, (255, 255, 255)), (constants.SCREEN_WIDTH//2-100, constants.SCREEN_HEIGHT//2-50))
        
        self.continue_button.draw(self.screen)
        self.quit_button.draw(self.screen)

        



