import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))  # White platform 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen, camera):
        adjusted_rect = self.rect.move(-camera['x'], -camera['y'])
        screen.blit(self.image, adjusted_rect)

