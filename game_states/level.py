# game_states/level.py

import pygame
from entities.player import Player
from entities.enemy import Enemy

class Level:
    def __init__(self, display):
        self.display = display
        self.player = Player(100, 500)  # Player starts on the ground
        self.enemy = Enemy(400, 500)  # Enemy starts on the ground as well

    def run(self):
        running = True
        while running:
            keys = pygame.key.get_pressed()
            self.player.move(keys)  # Call the player's move method
            self.enemy.update(self.player.x)  # Update enemy based on the player's x position

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None

            self.display.fill((0, 0, 0))  # Clear screen to black
            self.player.draw(self.display)  # Draw the player
            self.enemy.draw(self.display)    # Draw the enemy

            pygame.display.flip()  # Update the display