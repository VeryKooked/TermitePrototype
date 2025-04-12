# game_states/mainmenuscreen.py
import pygame
from game_states.level import level  # Import the level function
from game_states.instructionsscreen import Instructions  # Import the Instructions class

class MainMenu:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 36)
        self.button_rect = pygame.Rect(300, 250, 200, 50)  # Start Game button
        self.instructions_button_rect = pygame.Rect(300, 320, 200, 50)  # Instructions button
        self.running = True

    def draw(self):
        self.screen.fill((0, 0, 0))  # Black background
        title = self.font.render("Main Menu", True, (255, 255, 255))
        title_rect = title.get_rect(center=(400, 100))
        self.screen.blit(title, title_rect)

        # Draw the "Start Game" button
        pygame.draw.rect(self.screen, (162, 42, 42), self.button_rect)  
        button_text = self.font.render("Start Game", True, (0, 0, 0)) 
        button_text_rect = button_text.get_rect(center=self.button_rect.center)
        self.screen.blit(button_text, button_text_rect)

        # Draw the "Instructions" button
        pygame.draw.rect(self.screen, (0, 0, 255), self.instructions_button_rect)  
        instructions_button_text = self.font.render("Instructions", True, (255, 255, 255))  
        instructions_button_text_rect = instructions_button_text.get_rect(center=self.instructions_button_rect.center)
        self.screen.blit(instructions_button_text, instructions_button_text_rect)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Mouse click event
                if self.button_rect.collidepoint(event.pos):  # Check if Start Game button is clicked
                    self.running = False  # Transition to level
                    return True
                if self.instructions_button_rect.collidepoint(event.pos):  # Check if Instructions button is clicked
                    return "instructions"  # Transition to instructions screen
        return None

    def run(self):
        while self.running:
            result = self.handle_events()
            if result == "instructions":
                instructions_screen = Instructions()  # Create an instructions screen
                instructions_screen.run()  # Show instructions screen
            elif result:
                return level()  # Start the game level
            self.draw()
        return None  # If game is closed, exit gracefully
