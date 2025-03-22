# main.py

import pygame
from game_states.main_menu import MainMenu
from game_states.level import Level

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Platformer")

def main():
    menu = MainMenu()  # Initialize main menu
    menu.run()  # Run the main menu

    level = Level()  # Initialize game level
    level.run(screen)  # Run the game level

if __name__ == "__main__":
    main()