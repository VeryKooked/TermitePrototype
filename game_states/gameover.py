import pygame
import sys

def gameoverscreen(screen):
    pygame.font.init()
    font = pygame.font.SysFont(None, 72)
    small_font = pygame.font.SysFont(None, 48)

    game_over_text = font.render("Game Over", True, (255, 0, 0))
    retry_text = small_font.render("Press R to Retry", True, (255, 255, 255))
    quit_text = small_font.render("Press Q to Quit", True, (255, 255, 255))

    clock = pygame.time.Clock()
    waiting = True

    while waiting:
        screen.fill((0, 0, 0))  # black background

        # Draw text centered
        screen.blit(game_over_text, game_over_text.get_rect(center=(400, 200)))
        screen.blit(retry_text, retry_text.get_rect(center=(400, 300)))
        screen.blit(quit_text, quit_text.get_rect(center=(400, 360)))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return "retry"
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        clock.tick(60)
