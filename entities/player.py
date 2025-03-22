# entities/player.py

import pygame
from entities.base import BaseEntity  # Ensure this import path matches your structure

class Player(BaseEntity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 50
        self.height = 50
        self.velocity = 5
        self.is_jumping = False
        self.jump_speed = 10
        self.gravity = 0.5
        self.vertical_velocity = 0
        self.on_ground = True
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys):
        if keys[pygame.K_LEFT]:  # Move left
            self.x -= self.velocity
        if keys[pygame.K_RIGHT]:  # Move right
            self.x += self.velocity
        if keys[pygame.K_SPACE] and self.on_ground:  # Jump
            self.is_jumping = True

        if self.is_jumping:
            self.jump()

        # Apply gravity
        if not self.on_ground:
            self.vertical_velocity += self.gravity
            self.y += self.vertical_velocity

        # Simulate ground collision
        if self.y >= 600 - self.height:
            self.y = 600 - self.height
            self.on_ground = True
            self.vertical_velocity = 0
        else:
            self.on_ground = False

        self.hitbox.topleft = (self.x, self.y)

    def jump(self):
        if self.is_jumping:
            self.vertical_velocity = -self.jump_speed
            self.is_jumping = False

    def draw(self, surface):
        # Draw the player as a blue rectangle
        self.hitbox = pygame.draw.rect(surface, (0, 128, 255), (self.x, self.y, self.width, self.height))