import pygame as pg
from src import constants
from src.components.button import Button

class MainMenu:
    def __init__(self, screen) -> None:

        pg.font.init()
        
        button_font = pg.font.SysFont('Arial', 20)
        self.screen = screen
        buttons = self.determine_button_layout()
        self.single_player = Button(buttons[0], "Single Player", button_font, constants.BLACK, constants.WHITE, constants.WHITE, constants.BLACK)
        self.multiplayer = Button(buttons[1], "Multiplayer", button_font, constants.BLACK, constants.WHITE, constants.WHITE, constants.BLACK)
        self.settings = Button(buttons[2], "Settings", button_font, constants.BLACK, constants.WHITE, constants.WHITE, constants.BLACK)
        self.high_scores = Button(buttons[3], "High Scores", button_font, constants.BLACK, constants.WHITE, constants.WHITE, constants.BLACK)
        self.credits = Button(buttons[4], "Credits", button_font, constants.BLACK, constants.WHITE, constants.WHITE, constants.BLACK)
        self.quit = Button(buttons[5], "Quit", button_font, constants.BLACK, constants.WHITE, constants.WHITE, constants.BLACK)
        
    
    def draw(self):
        self.screen.fill(constants.BLACK)
        self.single_player.draw(self.screen)
        self.multiplayer.draw(self.screen)
        self.settings.draw(self.screen)
        self.high_scores.draw(self.screen)
        self.credits.draw(self.screen)
        self.quit.draw(self.screen)


    def determine_button_layout(self):
        """
        Determines the layout of the buttons on the screen based on the screen size.
        Each button sould have the width of 3/6 of the screen width and height of 1/10 of the screen height.
        The buttons should be centered on the screen.

        Returns:
            array: [(x, y, width, height),] of tuples of the buttons
        """
        buttons = []
        for i in range(len(constants.MAIN_MENU_OPTIONS)):
            x = constants.SCREEN_WIDTH/6
            y = constants.SCREEN_HEIGHT/10 + (i*constants.SCREEN_HEIGHT/10)
            width = constants.SCREEN_WIDTH/6*4
            height = constants.SCREEN_HEIGHT/10
            buttons.append([x, y, width, height])
        return buttons


    
    
