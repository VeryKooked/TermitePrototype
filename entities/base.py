import pygame

class BaseEntity:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, dx, dy):
        """Move the entity by a certain amount."""
        self.rect.x += dx
        self.rect.y += dy

    def collide_with_platforms(self, platforms):
        """Check and resolve collisions with platforms."""
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                # If colliding from above (top collision)
                if self.rect.bottom > platform.rect.top and self.rect.top < platform.rect.top:
                    self.rect.bottom = platform.rect.top  # Place entity on top of platform
                    return True  # Collision resolved
        return False

    def draw(self, screen, color):
        """Draw the entity to the screen."""
        pygame.draw.rect(screen, color, self.rect)
