# main.py

import pygame
from game_states.main_menu import MainMenu
from game_states.gameplay import Gameplay

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Platformer Game")

def main():
    clock = pygame.time.Clock()
    running = True
    current_state = "main_menu"

    menu_state = MainMenu(screen)
    game_state = Gameplay(screen)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if current_state == "main_menu":
            current_state = menu_state.run()
        elif current_state == "gameplay":
            current_state = game_state.run()

        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()