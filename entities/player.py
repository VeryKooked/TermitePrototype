import pygame
from entities.base import Entity

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)
        self.color = (0, 0, 255)  # Blue color

    def update(self, keys, platforms):
        """Update player state"""
        # Basic movement
        if keys[pygame.K_LEFT]:
            self.vel_x = -5
        elif keys[pygame.K_RIGHT]:
            self.vel_x = 5
        else:
            self.vel_x = 0
        
        if keys[pygame.K_UP] and self.on_ground:
            self.vel_y = -15  # Jump speed

        # Apply movement and handle collisions
        self.move(platforms)

    def draw(self, screen, camera):
        pygame.draw.rect(screen, self.color, camera.apply(self))
