import pygame
from entities.player import Player
from entities.enemy import Enemy

class Level:
    def __init__(self, player):
        self.player = player
        self.platforms = [pygame.Rect(100, 300, 200, 10), pygame.Rect(300, 200, 200, 10)]  # platforms
        self.enemies = pygame.sprite.Group()

    def add_enemy(self, enemy):
        self.enemies.add(enemy)

    def update(self):
        self.player.update(gravity=1)
        for enemy in self.enemies:
            enemy.update()
            if enemy.rect.x < 0 or enemy.rect.x > 600:
                enemy.change_direction()

    def handle_input(self, keys):
        if keys[pygame.K_a]:  # Left
            self.player.move_left()
        elif keys[pygame.K_d]:  # Right
            self.player.move_right()
        elif keys[pygame.K_w]:  # Jump
            self.player.jump()

    def render(self, screen):
        screen.fill((0, 0, 0))  # Clear the screen
        pygame.draw.rect(screen, (0, 255, 0), self.player.rect)  # Draw the player
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 0, 255), platform)  # Draw platforms
        for enemy in self.enemies:
            pygame.draw.rect(screen, (255, 0, 0), enemy.rect)  # Draw enemies
