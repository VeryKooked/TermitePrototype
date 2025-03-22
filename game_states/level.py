# game_states/level.py

import pygame
from game_objects.player import Player
from game_objects.enemy import Enemy

class Level:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(100, 500)
        self.enemy = Enemy(400, 500)
        self.blocks = [pygame.Rect(200, 450, 100, 20), pygame.Rect(400, 350, 100, 20)]
        self.gravity_value = 0.5

    def run(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            # Apply gravity effect
            if self.player.y < 500:  # Prevent falling through the ground
                self.player.y += self.gravity_value

            # Collision with blocks
            for block in self.blocks:
                if self.player.hitbox.colliderect(block):
                    self.player.y = block.top - self.player.height
                    self.player.on_ground = True

            self.screen.fill((135, 206, 235))  # Sky blue background
            self.player.draw(self.screen)

            for block in self.blocks:
                pygame.draw.rect(self.screen, (0, 255, 0), block)  # Draw moving blocks

            self.enemy.draw(self.screen)  # Draw enemy (for future use)

            pygame.display.flip()
            clock.tick(60)

        return "main_menu"  # Return to main menu when done