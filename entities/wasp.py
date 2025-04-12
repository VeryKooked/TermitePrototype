import pygame
from entities.base import Entity

class Wasp(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 50, 50)  # Initialize with size 50x50
        self.image = pygame.Surface((15, 25))  # The actual surface of the enemy
        self.image.fill((255, 0, 0))  # Red color for the wasp
        self.health = 3  # Starting health
        self.speed = 1.4  # Movement speed towards the player
        self.rect = self.image.get_rect(topleft=(x, y))  # Rect for positioning
        self.font = pygame.font.Font(None, 24)  # Font for the name display
        self.active = False  # Starts inactive

    def update(self, player, camera, screen_width, screen_height):
        # Viewport rectangle based on the camera
        view_rect = pygame.Rect(camera['x'], camera['y'], screen_width, screen_height)

        # Only activate once the enemy is visible on screen
        if not self.active and self.rect.colliderect(view_rect):
            self.active = True
            print(f"Wasp at {self.rect.topleft} activated!")  # Debug message

        if not self.active:
            return  # Skip movement if not active

        # Movement toward player
        dx = player.rect.centerx - self.rect.centerx
        dy = player.rect.centery - self.rect.centery
        distance = max((dx**2 + dy**2) ** 0.5, 0.0001)  # Prevent divide by zero
        dx /= distance
        dy /= distance
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

    def draw(self, screen, camera):
        adjusted_rect = self.rect.move(-camera['x'], -camera['y'])  # Adjust for camera
        screen.blit(self.image, adjusted_rect)

        # Draw the label with the name "Wasp"
        label = self.font.render("Wasp", True, (255, 255, 255))
        label_rect = label.get_rect(center=(self.rect.centerx - camera['x'], self.rect.top - 10 - camera['y']))
        screen.blit(label, label_rect)
