import pygame as pg
from src.constants import BLACK, WHITE

class Button:
    """
    A class to represent a button in the game.
    The class allows for different button types to be created.
    """
    def __init__(self, *args):
        """
        Initializes the button object.
        
        Args:
            x (int): The x-coordinate of the button.
            y (int): The y-coordinate of the button.
            width (int): The width of the button.
            height (int): The height of the button.
            text (str): The text to be displayed on the button.
            font (pg.font.Font): The font of the text.
            color (tuple): The color of the button.
            hover_color (tuple, optional): The color of the button when hovered over
            text_color (tuple, optional): The color of the text on the button
            hover_alt_text_color (tuple, optional): The color of the text on the button when hovered over
            """
        
        if isinstance(args[0], list):
            aux = []
            for element in args[0]:
                aux.append(element)
            for arg in args[1:]:
                aux.append(arg)
            args = aux

            self.rect = pg.Rect(args[0], args[1], args[2], args[3])
            self.text = args[4]
            self.font = args[5]
            self.color = args[6]
            self.hover_color = args[7] if len(args) >= 8 else self.color
            self.text_color = args[8] if len(args) >= 9 else BLACK
            self.hover_alt_text_color = args[9] if len(args) == 10 else self.text_color


    
    def draw(self, surface):
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.text_surface = self.font.render(self.text, True, self.hover_alt_text_color)
            self.text_rect = self.text_surface.get_rect(center=self.rect.center)
            pg.draw.rect(surface, self.hover_color, self.rect)
        else:
            self.text_surface = self.font.render(self.text, True, self.text_color)
            self.text_rect = self.text_surface.get_rect(center=self.rect.center)
            pg.draw.rect(surface, self.color, self.rect)

        surface.blit(self.text_surface, self.text_rect)

    def is_clicked(self):
        mouse_pos = pg.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0]:  # Left mouse button
                return True
        return False
