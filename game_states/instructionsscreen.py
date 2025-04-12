# game_states/instructionsscreen.py
import pygame

class Instructions:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 36)
        self.running = True
        self.back_button = pygame.Rect(300, 450, 200, 50)

    def draw(self):
        self.screen.fill((0, 0, 0))  # Black background
        title = self.font.render("Instructions", True, (255, 255, 255))
        title_rect = title.get_rect(center=(400, 100))
        self.screen.blit(title, title_rect)

        instructions_text = [
            "A - Move Left",
            "D - Move Right",
            "Space - Jump",
            "Up arrow key - Pick up item",
        ]
        
        y_offset = 200
        for text in instructions_text:
            render_text = self.font.render(text, True, (255, 255, 255))
            text_rect = render_text.get_rect(center=(400, y_offset))
            self.screen.blit(render_text, text_rect)
            y_offset += 50

        # Draw back button
        pygame.draw.rect(self.screen, (255, 0, 0), self.back_button)
        button_text = self.font.render("Back", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=self.back_button.center)
        self.screen.blit(button_text, button_text_rect)

        pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return "quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.collidepoint(event.pos):
                    self.running = False
                    return "back"
        return None

    def run(self):
        while self.running:
            result = self.handle_events()
            if result == "back":
                return  # Return to the main menu
            elif result == "quit":
                pygame.quit()
                exit()
            self.draw()
