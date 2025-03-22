# enemy class

import pygame
from game_object import GameObject

class Enemy(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 40
        self.height = 40
        self.hitbox = pygame.Rect(x, y, self.width, self.height)

    def update(self):
        # Add enemy behavior here (movement, etc.)
        pass

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.hitbox)  # Draw a red rectangle for the enemy