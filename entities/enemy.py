import pygame
from entities.base import Entity

class Enemy(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)
        self.image = pygame.Surface((15, 25))
        self.image.fill((255, 0, 0))
        self.health = 3
        self.speed = 1.4
        self.rect = self.image.get_rect(topleft=(x, y))
        self.font = pygame.font.Font(None, 24)
        self.active = False  # Start inactive

    def update(self, player, camera, screen_width, screen_height):
        # Viewport rectangle based on the camera
        view_rect = pygame.Rect(camera['x'], camera['y'], screen_width, screen_height)

        # Only activate once, ever
        if not self.active and self.rect.colliderect(view_rect):
            self.active = True
            print(f"Enemy at {self.rect.topleft} activated!")  # Debug message

        if not self.active:
            return  # Skip movement if not active

        # Movement toward player
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distance = max((dx**2 + dy**2) ** 0.5, 0.0001)
        dx /= distance
        dy /= distance
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, screen, camera):

        adjusted_rect = self.rect.move(-camera['x'], -camera['y'])
        screen.blit(self.image, adjusted_rect)

        label = self.font.render("Wasp", True, (255, 255, 255))
        label_rect = label.get_rect(center=(self.rect.centerx - camera['x'], self.rect.top - 10 - camera['y']))
        screen.blit(label, label_rect)
