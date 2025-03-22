# player/termite man :0

import pygame
from game_object import GameObject

class Player(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.width = 50
        self.height = 50
        self.velocity = 5
        self.is_jumping = False
        self.jump_height = 10
        self.hitbox = pygame.Rect(x, y, self.width, self.height)

    def move(self, keys):
        if keys[pygame.K_a]:
            self.x -= self.velocity
        if keys[pygame.K_d]:
            self.x += self.velocity
        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.is_jumping = True

        if self.is_jumping:
            self.jump()

        self.hitbox.topleft = (self.x, self.y)

    def jump(self):
        self.y -= self.jump_height
        self.is_jumping = False

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 128, 255), self.hitbox)  # Draw a blue rectangle for the player