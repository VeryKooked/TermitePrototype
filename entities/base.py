import pygame

class Entity:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.vel_x = 0
        self.vel_y = 0
        self.on_ground = False  # check if entity on platform

    def move(self, platforms):
        """Move the entity while checking for collisions"""
        self.rect.x += self.vel_x
        self.collide_with_platforms(platforms, 'x')

        self.rect.y += self.vel_y
        self.collide_with_platforms(platforms, 'y')

    def collide_with_platforms(self, platforms, axis):
        """Check for collisions with platforms on specified axis"""
        self.on_ground = False  #
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if axis == 'x':  
                    if self.vel_x > 0:  # Moving right
                        self.rect.right = platform.rect.left
                    elif self.vel_x < 0:  # Moving left
                        self.rect.left = platform.rect.right
                    self.vel_x = 0  # Stop horizontal movement
                elif axis == 'y':  # Vertical collision
                    if self.vel_y > 0:  # Falling
                        self.rect.bottom = platform.rect.top
                        self.on_ground = True  
                        self.vel_y = 0  
                    elif self.vel_y < 0: 
                        self.rect.top = platform.rect.bottom
                        self.vel_y = 0  # Stop upward movement
        if axis == 'y' and not self.on_ground:
            self.vel_y += 1  
        elif self.on_ground:
            self.vel_y = 0  
