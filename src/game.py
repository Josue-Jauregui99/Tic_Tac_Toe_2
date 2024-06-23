from src.views.gameplay_view import GameplayView
import pygame as pg
from src import constants, computer_player
import random


class Game_Loop:
    def __init__(self, screen, game_mode):
        self.screen = screen
        self.running = True
        self.game = GameplayView(screen)
        self.board = ['','','','','','','','','']
        self.players = ['X', 'O']
        self.sectors = []
        self.turn = 0
        self.game_mode = game_mode
        if self.game_mode == 'single':
            self.computer = computer_player.ComputerPlayer(self.players[1])
        
        for n in range(9):
            self.sectors.append(
                pg.Rect(
                    constants.MIN_BOARD_WIDTH + (n % 3) * constants.DISTANCE_VERTICAL,
                    constants.MIN_BOARD_HEIGHT + (n // 3) * constants.DISTANCE_HORIZONTAL,
                    constants.DISTANCE_VERTICAL,
                    constants.DISTANCE_HORIZONTAL
                    )
            )
        self.run()

    
    
    def run(self):
        turns = 0
        status = 'running'
        while self.run:
            self.game.draw_board(self.board, self.sectors)
            pg.display.update()

            if self.game_mode == 'single':
                if self.turn == 1:
                    move = self.computer.get_move(self.board)
                    if move != -1:
                        pg.time.wait(500)
                        self.board[move] = self.players[self.turn]
                        if self.check_winner(self.turn):
                            status = 'winner'
                            self.run = False
                    elif turns == 8:
                        self.run = False
                        status = 'draw'
                    turns += 1
                    self.turn = (self.turn + 1) % 2

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()
                    sector = self.check_sector_click(self.sectors, self.board, mouse_pos)
                    if sector is not None:
                        self.board[sector] = self.players[self.turn]

                        if turns>=4 and self.check_winner(self.turn):
                            status = 'winner'
                            self.run = False
                        elif turns == 8:
                            self.run = False
                            status = 'draw'
                        turns += 1
                        self.turn = (self.turn + 1) % 2
            
            if not self.run:
                self.turn = (self.turn + 1) % 2
                self.endign_screen(status)
                turns = 0

            

                            
            pg.time.Clock().tick(60)
    
    def check_sector_click(self, sectors, board, mouse_pos):
        for n, sector in enumerate(sectors):
            if sector.collidepoint(mouse_pos) and board[n] == '':
                return n
        return None

    def check_winner(self, current_player):
        winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] == self.players[current_player]:
                return True
        return False
    
    def coin_flip(self):
        return random.randint(0, 1)
    
    def reset(self):
        self.board = ['','','','','','','','','']
        self.turn = self.coin_flip()
        self.run = True
    
    def endign_screen(self, status):

        selection = False
        while not selection:
            self.game.game_over_screen( status, self.players[self.turn])
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_pos = pg.mouse.get_pos()
                    if self.game.continue_button.is_clicked():
                        self.reset()
                        selection = True
                    if self.game.quit_button.is_clicked():
                        selection = True
                        self.running = False
            
            pg.display.update()
            pg.time.Clock().tick(60)