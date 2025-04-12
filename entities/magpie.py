import pygame
from entities.base import Entity

class Magpie(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 60, 60)
        self.image = pygame.Surface((60, 60))
        self.image.fill((255, 255, 255))
        self.start_x = x
        self.start_y = y
        self.swoop_speed = 8  # Fast dive
        self.state = 'waiting'  # 'waiting', 'swooping', 'resetting'
        self.timer = 0
        self.delay = 120  # Frames to wait before next swoop
        self.rect = self.image.get_rect(topleft=(x, y))
        self.font = pygame.font.Font(None, 24)
        self.active = False
        self.damage = 4

    def update(self, player, camera, screen_width, screen_height):
        # Viewport rectangle based on the camera
        view_rect = pygame.Rect(camera['x'], camera['y'], screen_width, screen_height)

        if not self.active and self.rect.colliderect(view_rect):
            self.active = True
            print(f"Magpie at {self.rect.topleft} activated!")

        if not self.active:
            return

        if self.state == 'waiting':
            self.timer += 1
            if self.timer >= self.delay:
                self.state = 'swooping'
                self.timer = 0

        elif self.state == 'swooping':
            self.rect.y += self.swoop_speed
            if self.rect.top > screen_height + 200:  # Off-screen bottom
                self.state = 'resetting'

        elif self.state == 'resetting':
            self.rect.topleft = (self.start_x, self.start_y)
            self.state = 'waiting'
            self.timer = 0

    def draw(self, screen, camera):
        adjusted_rect = self.rect.move(-camera['x'], -camera['y'])
        screen.blit(self.image, adjusted_rect)

        label = self.font.render("Magpie", True, (255, 255, 255))
        label_rect = label.get_rect(center=(self.rect.centerx - camera['x'], self.rect.top - 10 - camera['y']))
        screen.blit(label, label_rect)
