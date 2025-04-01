import pygame
from entities.player import Player
from entities.enemy import Enemy

class Level:
    def __init__(self, player):
        self.player = player  # Store player object for the level
        

    def update(self):
        """Update the level state"""
        # Update the player position 
        pass

    def draw(self, screen):
        """Draw the level's elements to the screen"""
        # Draw level elements, to be inlculuded
        pass
