import pygame
from entities.base import Entity

class Ant(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)  # Assuming 'Entity' class has x, y position
        self.width = 50
        self.height = 50
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((255, 255, 0))  # Yellow color
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        # Floating logic or animation logic can go here, for now it just stays still
        pass

    def draw(self, screen, camera):
        # Draw the floating square
        adjusted_rect = self.rect.move(-camera['x'], -camera['y'])
        screen.blit(self.image, adjusted_rect)
