import pygame
from entities.player import Player

class Leafarmour:
    def __init__(self, x, y):
        self.width = 10
        self.height = 25
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((34, 139, 34))  # green leaf armour
        self.rect = self.image.get_rect(topleft=(x, y))
        self.collected = False

    def draw(self, screen, camera):
        if not self.collected:
            adjusted_rect = self.rect.move(-camera['x'], -camera['y'])
            screen.blit(self.image, adjusted_rect)
    



    def collect(self, player_rect, keys, player): # collection mechanic
        if not self.collected and self.rect.colliderect(player_rect):
            if keys[pygame.K_UP]:
                self.collected = True
                player.has_leafarmour = True  
                player.shield_points = 3      # leafarmour will give 3 shield points everytime picked up
                print("Leafarmour collected! Shield activated.")
                return True
        return False