import pygame
from entities.player import Player
from entities.enemy import Enemy

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Platformer")

def main():
    clock = pygame.time.Clock()
    player = Player(100, 500)  # Initial position of the player
    enemy = Enemy(400, 500)    # Initial position of the enemy
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player.move(keys)  # Move player based on key inputs

        # Calculate camera offset to center on the player
        camera_offset_x = player.x - (SCREEN_WIDTH / 2) + (player.width / 2)

        # Prevent camera from moving left beyond the starting point
        camera_offset_x = max(0, camera_offset_x)

        # Rendering
        screen.fill((0, 0, 0))  # Clear the screen

        # Draw player and enemy with camera offset
        player.draw(screen, camera_offset_x)
        enemy.draw(screen, camera_offset_x)