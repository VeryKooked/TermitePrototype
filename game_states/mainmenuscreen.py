import pygame
from game_states.level import level  
from game_states.instructionsscreen import Instructions  

class MainMenu:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 36)
        self.button_rect = pygame.Rect(300, 250, 200, 50)  
        self.instructions_button_rect = pygame.Rect(300, 320, 200, 50)  #
        self.running = True

    def draw(self):
        self.screen.fill((0, 0, 0))  
        title = self.font.render("Main Menu", True, (255, 255, 255))
        title_rect = title.get_rect(center=(400, 100))
        self.screen.blit(title, title_rect)

        # draw the start game button
        pygame.draw.rect(self.screen, (162, 42, 42), self.button_rect)  
        button_text = self.font.render("Start Game", True, (0, 0, 0)) 
        button_text_rect = button_text.get_rect(center=self.button_rect.center)
        self.screen.blit(button_text, button_text_rect)

        # draw the instructions
        pygame.draw.rect(self.screen, (0, 0, 255), self.instructions_button_rect)  
        instructions_button_text = self.font.render("Instructions", True, (255, 255, 255))  
        instructions_button_text_rect = instructions_button_text.get_rect(center=self.instructions_button_rect.center)
        self.screen.blit(instructions_button_text, instructions_button_text_rect)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  # mouse click
                if self.button_rect.collidepoint(event.pos):  
                    self.running = False  # transition to level
                    return True
                if self.instructions_button_rect.collidepoint(event.pos):  
                    return "instructions"  # transition to instructions screen
        return None

    def run(self):
        while self.running:
            result = self.handle_events()
            if result == "instructions":
                instructions_screen = Instructions()  # create instructions screen
                instructions_screen.run()  # show instructions screen
            elif result:
                return level()  # start game
            self.draw()
        return None 
