import pygame
from entities.base import BaseEntity
from game_states.camera import Camera

class Enemy(BaseEntity):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)  # Call the constructor of BaseEntity

    def move(self, platforms):
        # Simple AI: Move back and forth
        self.rect.x += 2  # Move right
        self.apply_gravity(platforms)

    def apply_gravity(self, platforms):
        self.rect.y += 0.5  # Gravity applied to enemy
        self.collide_with_platforms(platforms)

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (255, 0, 0), camera.apply(self))

