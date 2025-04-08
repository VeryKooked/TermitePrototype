import pygame
from entities.base import Entity

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)  # size of enemy
        self.image = pygame.Surface((50, 50))  # rectangle for the enemy
        self.image.fill((255, 0, 0))  # red colour

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.rect)
