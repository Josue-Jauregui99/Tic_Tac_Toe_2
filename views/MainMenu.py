import pygame

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

        self.game_title = self.font.render("TicTacToe!", True, (255, 255, 255))  # White text
        self.title_text = self.font.render("Main Menu", True, (255, 255, 255))  # White text
        self.title_rect = self.game_title.get_rect(center=(320, 50))
        self.text_rect = self.title_text.get_rect(center=(320, 150))

        
        # Button settings
        self.button_color = (0, 255, 0)  # Green
        self.button_hover_color = (0, 150, 0)  # Darker green
        self.button_rect = pygame.Rect(250, 200, 140, 50)
        self.button_text = self.font.render("Click Me!", True, (0, 0, 0))  # Black text

        
    def draw(self):
        # Button hover effect
        mouse_pos = pygame.mouse.get_pos()
        if self.button_rect.collidepoint(mouse_pos):
            color = self.button_hover_color
        else:
            color = self.button_color
        
        # Draw button
        pygame.draw.rect(self.screen, color, self.button_rect)
        self.screen.blit(self.button_text, (self.button_rect.x + 5, self.button_rect.y + 5))
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                print("Button clicked!")
                # Perform button action here