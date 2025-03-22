import pygame
from entities.base import Entity

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)
        self.color = (255, 0, 0)  # Red color
        self.vel_x = 2  # Enemy speed

    def update(self, platforms):
        """Update enemy state (simple AI or random movement)"""
        self.move(platforms)

    def draw(self, screen, camera):
        pygame.draw.rect(screen, self.color, camera.apply(self))
