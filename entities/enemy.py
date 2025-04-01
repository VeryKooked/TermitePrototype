import pygame
from entities.base import Entity

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)  # Enemy size 
        self.image = pygame.Surface((50, 50))  # Enemy image (just a rectangle for now)
        self.image.fill((255, 0, 0))  # Red enemy 

    def update(self):
        """Update the enemy’s state (movement, etc.)"""
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
