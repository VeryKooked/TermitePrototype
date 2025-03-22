# entities/enemy.py

import pygame
from entities.base import BaseEntity

class Enemy(BaseEntity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 50
        self.height = 50
        self.speed = 2
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, player_x):
        # The enemy starts from its initial position
        if self.x < player_x:  # Follow the player if enemy is to the left
            self.x += self.speed
        elif self.x > player_x:  # Optional: to reset position if the enemy goes right
            self.x -= self.speed

        # Keep the enemy on the ground
        self.y = 500  # Set a fixed y-position for the enemy on the ground

def draw(self, surface, camera_offset_x):
    # Draw the enemy considering camera offset
    self.hitbox = pygame.draw.rect(surface, (255, 0, 0), (self.x - camera_offset_x, self.y, self.width, self.height))