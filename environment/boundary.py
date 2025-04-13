import pygame

class Walls:
    def __init__(self, screen_width, floor_y, wall_thickness=50, wall_height=600):
        self.left_wall = pygame.Rect(0, floor_y - wall_height, wall_thickness, wall_height)
        self.right_wall = pygame.Rect(screen_width - wall_thickness, floor_y - wall_height, wall_thickness, wall_height)
        self.color = (100, 100, 100)  # Dark gray

    def draw(self, screen, camera):
        # Adjust for camera offset
        left_rect = self.left_wall.move(-camera['x'], -camera['y'])
        right_rect = self.right_wall.move(-camera['x'], -camera['y'])
        pygame.draw.rect(screen, self.color, left_rect)
        pygame.draw.rect(screen, self.color, right_rect)

    def get_rects(self):
        return [self.left_wall, self.right_wall]
