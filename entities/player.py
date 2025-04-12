import pygame
from entities.base import Entity  

class Player(Entity):
    def __init__(self, x, y):
        # Set width and height
        self.width = 20 
        self.height = 40
        super().__init__(x, y, self.width, self.height)  # Pass width and height to the parent constructor
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((0, 0, 255))  # Blue color 
        self.rect = self.image.get_rect(topleft=(x, y))

        self.health = 5  # Player starts with 5 HP
        self.has_leafblade = False  # Track item possession
        self.velocity_x = 0  
        self.velocity_y = 0  #
        self.speed = 2.4  # Movement speed
        self.gravity = 0.3  # Gravity strength
        self.jump_strength = -9  # Jump strength
        self.on_ground = False  
        
    def inputs(self, platforms):
        self.velocity_x = 0  # Reset horizontal velocity each frame

        # movement-horizontal
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.velocity_x = -self.speed
        if keys[pygame.K_RIGHT]:
            self.velocity_x = self.speed
        
        # jump
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = self.jump_strength
            self.on_ground = False  
        
        # gravity
        if not self.on_ground:
            self.velocity_y += self.gravity  

        # Update position
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        
        # platform collision
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # Falling down
                    self.rect.bottom = platform.rect.top
                    self.velocity_y = 0
                    self.on_ground = True
                    break
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)  # draw player
