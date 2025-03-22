# main.py

import pygame
from game_states.main_menu import MainMenu
from game_states.level import Level

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Termite Game Prototype")

def main():
    clock = pygame.time.Clock()
    running = True
    current_state = "main_menu"

    main_menu = MainMenu(screen)
    level = Level(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_state == "main_menu":
            current_state = main_menu.run()
        elif current_state == "level":
            current_state = level.run()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()