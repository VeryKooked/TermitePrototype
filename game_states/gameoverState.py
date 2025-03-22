# game_states/game_over_state.py

import pygame

class GameOverState:
    def __init__(self, display):
        self.display = display
        self.font = pygame.font.Font(None, 74)

    def run(self):
        while True:
            self.display.fill((0, 0, 0))  # Black background
            game_over_text = self.font.render('Game Over', True, (255, 0, 0))
            restart_text = self.font.render('Press ENTER to Restart', True, (255, 255, 255))

            self.display.blit(game_over_text, (self.display.get_width() // 2 - game_over_text.get_width() // 2, 200))
            self.display.blit(restart_text, (self.display.get_width() // 2 - restart_text.get_width() // 2, 350))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "level"  # Restart the level state

            pygame.display.flip()