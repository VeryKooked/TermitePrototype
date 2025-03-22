# entities/enemy.py

import pygame
from entities.base import Base

class Enemy(Base):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)  # Width and Height for the enemy
    
    def draw(self, surface, camera_offset_x):
        pygame.draw.rect(surface, (255, 0, 0), (self.x - camera_offset_x, self.y, self.width, self.height))