# entities/leafblade.py
import pygame
from entities.player import Player


class Leafblade:
    def __init__(self, x, y):
        self.width = 10
        self.height = 25
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((34, 139, 34))  # Forest green for leaf look
        self.rect = self.image.get_rect(topleft=(x, y))
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, self.rect)

    def collect(self, player_rect, keys, player):
        if not self.collected and self.rect.colliderect(player_rect):
            if keys[pygame.K_UP]:
                self.collected = True
                player.has_leafblade = True  # <-- important: update instance, not class
                print("Leafblade collected!")  
                return True
        return False



