import pygame

class Platform:
    def __init__(self, x, y, width, height):
        self.image = pygame.Surface((width, height))
        self.image.fill((100, 100, 100))  # Grey platform
        self.rect = self.image.get_rect(topleft=(x, y))  # Assigns rect

