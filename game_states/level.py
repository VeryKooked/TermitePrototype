# game_states/level.py

import pygame
from entities.player import Player
from entities.enemy import Enemy
from game_states.game_over_state import GameOverState

class Level:
    def __init__(self, display):
        self.display = display
        self.clock = pygame.time.Clock()
        self.player = Player(100, 500)
        self.enemies = [Enemy(400, 500)]
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            keys = pygame.key.get_pressed()
            self.player.move(keys)

            # Update enemy positions
            for enemy in self.enemies:
                enemy.move()

            # Check for game over condition (example: player falls below screen)
            if self.player.y > 600:
                return "game_over"

            self.display.fill((135, 206, 235))  # Sky blue background
            self.player.draw(self.display)
            for enemy in self.enemies:
                enemy.draw(self.display)

            pygame.display.flip()
            self.clock.tick(60)

        return "main_menu"