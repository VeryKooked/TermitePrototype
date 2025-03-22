# game_states/main_menu.py

import pygame

class MainMenu:
    def __init__(self):
        self.font = pygame.font.Font(None, 74)
        self.title_text = self.font.render("Main Menu", True, (255, 255, 255))
        self.start_text = self.font.render("Press ENTER to start", True, (255, 255, 255))

    def display(self, screen):
        screen.fill((0, 0, 0))  # Black background
        screen.blit(self.title_text, (200, 100))  # Center title
        screen.blit(self.start_text, (150, 300))  # Center start text

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Start game on ENTER
                        return

            pygame.display.update()