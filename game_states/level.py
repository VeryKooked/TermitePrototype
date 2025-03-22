# game_states/level.py

import pygame
from entities.player import Player
from entities.enemy import Enemy

class Level:
    def __init__(self):
        self.player = Player(100, 500)  # Initial position of the player
        self.enemy = Enemy(400, 500)     # Initial position of the enemy

    def run(self, screen):
        clock = pygame.time.Clock()
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
            keys = pygame.key.get_pressed()
            self.player.move(keys)  # Update player position
        
            # Camera offset logic
            camera_offset_x = self.player.x - (800 / 2) + (self.player.width / 2)
            camera_offset_x = max(0, camera_offset_x)  # Prevent going off-screen
            
            screen.fill((0, 0, 0))  # Clear the screen
            self.player.draw(screen, camera_offset_x)  # Draw player
            self.enemy.draw(screen, camera_offset_x)    # Draw enemy
            
            pygame.display.update()  # Update the display
            clock.tick(60)  # Ensure the game runs at 60 FPS