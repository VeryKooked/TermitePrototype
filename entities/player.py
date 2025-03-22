import pygame
from entities.base import BaseEntity
from game_states.camera import Camera

class Player(BaseEntity):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)  # Call the constructor of BaseEntity
        self.velocity = 5
        self.is_jumping = False
        self.jump_count = 10
        self.gravity = 0.5

    def move(self, keys, platforms):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocity

        if not self.is_jumping:
            if keys[pygame.K_SPACE]:
                self.is_jumping = True
        else:
            if self.jump_count >= -10:
                neg = 1
                if self.jump_count < 0:
                    neg = -1
                self.rect.y -= (self.jump_count ** 2) * 0.5 * neg
                self.jump_count -= 1
            else:
                self.is_jumping = False
                self.jump_count = 10

        self.apply_gravity(platforms)

    def apply_gravity(self, platforms):
        if not self.is_jumping:
            self.rect.y += self.gravity
        self.collide_with_platforms(platforms)

    def draw(self, screen, camera):
        pygame.draw.rect(screen, (0, 0, 255), camera.apply(self))

