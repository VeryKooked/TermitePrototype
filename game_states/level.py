# game_states/level.py

import pygame
from entities.player import Player
from entities.enemy import Enemy

class Level:
    def __init__(self, display):
        self.display = display
        self.player = Player(100, 500)  # Start position for the player
        self.enemy = Enemy(400, 500)    # Position for the enemy on the ground
        self.camera_offset_x = 0       # Initialize camera offset

    def run(self):
        running = True
        while running:
            keys = pygame.key.get_pressed()
            self.player.move(keys)  # Move the player

            # Update camera offset to follow player
            # Center the player's position with respect to the screen
            self.camera_offset_x = self.player.x - (self.display.get_width() / 2) + (self.player.width / 2)

            # Keep the camera within the bounds (if applicable)
            self.camera_offset_x = max(0, self.camera_offset_x)  # Prevent moving the camera left off-screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None

            self.display.fill((0, 0, 0))  # Clear the screen to black

            # Draw the player and enemy with the camera offset applied
            self.player.draw(self.display, self.camera_offset_x)  # Pass the camera offset when drawing
            self.enemy.draw(self.display, self.camera_offset_x)    # Draw enemy

            pygame.display.flip()  # Update the display