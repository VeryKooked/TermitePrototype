import pygame
from entities.base import Entity

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)  # size of enemy
        self.image = pygame.Surface((15, 25))  # visual rectangle
        self.image.fill((255, 0, 0))  # red color
        self.health = 3  # Enemy starts with 3 HP
        self.speed = 1.4  # movement speed toward player
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, player):
        # Calculate the direction vector from enemy to player
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery

        # Normalize direction to prevent faster diagonal movement
        distance = max((dx**2 + dy**2) ** 0.5, 0.0001)  # avoid division by 0
        dx /= distance
        dy /= distance

        # Move enemy toward player
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

