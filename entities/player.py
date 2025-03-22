# entities/player.py

import pygame
from entities.base import Base

class Player(Base):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)  # Initialize with width and height
        self.velocity = 5
        self.is_jumping = False
        self.jump_speed = 10
        self.gravity = 0.5
        self.vertical_velocity = 0
        self.on_ground = True

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:  # Prevent going off-screen
            self.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.x < 800 - self.width:  # Prevent going off-screen
            self.x += self.velocity
        if keys[pygame.K_SPACE] and self.on_ground:  # Jump logic
            self.is_jumping = True
            self.vertical_velocity = -self.jump_speed
            self.on_ground = False

        # Gravity effect
        if not self.on_ground:
            self.vertical_velocity += self.gravity
            self.y += self.vertical_velocity
        
        # Simulate ground collision (Assuming ground is at y = 500)
        if self.y >= 500 - self.height:
            self.y = 500 - self.height
            self.on_ground = True
            self.vertical_velocity = 0
        else:
            self.on_ground = False

    def draw(self, surface, camera_offset_x):
        pygame.draw.rect(surface, (0, 128, 255), (self.x - camera_offset_x, self.y, self.width, self.height))