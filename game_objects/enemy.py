# enemy.py

import pygame
from objects import game_object

class Enemy(game_object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 50
        self.height = 50
        self.hitbox = pygame.Rect(x, y, self.width, self.height)

    def update(self):
        # You can add enemy behavior here
        pass

    def draw(self, surface):
        self.hitbox = pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))