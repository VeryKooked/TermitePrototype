import pygame

class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def update(self, target):
        """Center the camera on the target (player)"""
        self.camera.x = target.rect.x - self.width // 2 + target.rect.width // 2
        self.camera.y = target.rect.y - self.height // 2 + target.rect.height // 2

        # Prevent the camera from moving past the left or top boundaries
        self.camera.x = max(0, self.camera.x)
        self.camera.y = max(0, self.camera.y)

    def apply(self, entity):
        """Apply camera offset to an entity"""
        return entity.rect.move(-self.camera.x, -self.camera.y)

    def apply_rect(self, rect):
        """Apply camera offset to a rectangle (e.g., platforms)"""
        return rect.move(-self.camera.x, -self.camera.y)
