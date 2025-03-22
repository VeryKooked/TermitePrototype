import pygame

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50

    def draw(self, surface, camera_offset_x):
        # Draw the enemy as a red rectangle
        pygame.draw.rect(surface, (255, 0, 0), (self.x - camera_offset_x, self.y, self.width, self.height))