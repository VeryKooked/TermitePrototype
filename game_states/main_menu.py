# game_states/main_menu.py

import pygame

class MainMenu:
    def __init__(self, display):
        self.display = display
        self.font = pygame.font.Font(None, 74)

    def run(self):
        while True:
            self.display.fill((0, 0, 0))  # Black background
            title_text = self.font.render('Main Menu', True, (255, 255, 255))
            start_text = self.font.render('Press ENTER to Start', True, (255, 255, 255))

            self.display.blit(title_text, (self.display.get_width() // 2 - title_text.get_width() // 2, 100))
            self.display.blit(start_text, (self.display.get_width() // 2 - start_text.get_width() // 2, 300))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "level"  # Transition to level state

            pygame.display.flip()