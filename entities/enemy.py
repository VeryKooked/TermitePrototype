# entities/enemy.py

import pygame
from .base import BaseEntity

class Enemy(BaseEntity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 50
        self.height = 50
        self.speed = 2
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        self.x += self.speed
        # Reverse direction upon reaching the screen edges
        if self.x < 0 or self.x > 750:  # Assuming screen width is 800
            self.speed = -self.speed

    def draw(self,