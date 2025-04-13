import pygame

class Entity:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False

    def collide_with_platforms(self, platforms, axis):
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform):
                if axis == 'x':
                    if self.vel_x > 0:
                        self.rect.right = platform.left
                    elif self.vel_x < 0:
                        self.rect.left = platform.right
                    self.vel_x = 0
                elif axis == 'y':
                    if self.vel_y > 0:
                        self.rect.bottom = platform.top
                        self.on_ground = True
                        self.vel_y = 0
                    elif self.vel_y < 0:
                        self.rect.top = platform.bottom
                        self.vel_y = 0

        if axis == 'y' and not self.on_ground:
            self.vel_y += 1
        elif self.on_ground:
            self.vel_y = 0

    def move(self, platforms):
        self.rect.x += self.vel_x
        self.collide_with_platforms(platforms, 'x')

        self.rect.y += self.vel_y
        self.collide_with_platforms(platforms, 'y')
