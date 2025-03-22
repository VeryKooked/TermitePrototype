
import pygame
from game_objects.player import Player
from game_objects.enemy import Enemy

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Game Initialization
player = Player(100, SCREEN_HEIGHT - 70)
enemy = Enemy(300, SCREEN_HEIGHT - 70)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)

        # Clear screen
        screen.fill((135, 206, 250))  # Light blue background

        # Draw elements
        player.draw(screen)
        enemy.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()