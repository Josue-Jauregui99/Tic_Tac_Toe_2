from utils import constants, helpers
from views.gameplay import GameplayView
import pygame as pg

def game_loop(screen):
    run = True
    game = GameplayView()
    board = ['','','','','','','','','']
    players = ['X', 'O']
    sectors = []
    turn = 0
    for n in range(9):
        sectors.append(pg.Rect(constants.MIN_BOARD_WIDTH + (n % 3) * constants.DISTANCE_HORIZONTAL, constants.MIN_BOARD_HEIGHT + (n // 3) * constants.DISTANCE_VERTICAL, constants.DISTANCE_HORIZONTAL, constants.DISTANCE))

    while run:

        game.draw_board(screen, board, sectors)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = pg.mouse.get_pos()
                sector = helpers.check_sector_click(sectors, board, mouse_pos)
                if sector is not None:
                    print('Valid move!')
                    board[sector] = players[turn]
                    turn = (turn + 1) % 2
        pg.display.update()

    
def main():

    pg.init()
    pg.font.init()

    screen = pg.display.set_mode([constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT])
    game_loop(screen)
    pg.quit()

if __name__ == '__main__':
    main()