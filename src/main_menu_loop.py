import pygame as pg
from src.views.main_menu_view import MainMenu
from src.game import Game_Loop 

class MainMenuLoop:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.main_menu_view = MainMenu(screen)
        self.running = True
        self.run()
    
    def run(self):
        while self.running:
            self.main_menu_view.draw()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    if self.main_menu_view.single_player.is_clicked():
                        Game_Loop(self.screen)
                    if self.main_menu_view.multiplayer.is_clicked():
                        print("Multiplayer")
                    if self.main_menu_view.settings.is_clicked():
                        print("Settings")
                    if self.main_menu_view.high_scores.is_clicked():
                        print("High Scores")
                    if self.main_menu_view.credits.is_clicked():
                        print("Credits")
                    if self.main_menu_view.quit.is_clicked():
                        self.running = False
            pg.display.update()
            pg.time.Clock().tick(60)
        pg.quit()
    

