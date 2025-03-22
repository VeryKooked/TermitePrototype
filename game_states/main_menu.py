# game_states/main_menu.py

import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.running = True

    def run(self):
        while self.running:
            self.screen.fill((0, 0, 0))  # Black background
            title_text = self.font.render('Main Menu', True, (255, 255, 255))
            self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

            start_text = self.font.render('Press ENTER to Start', True, (255, 255, 255))
            self.screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "level"  # Switch to level state

            pygame.display.flip()
        return None