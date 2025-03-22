# entities/base.py

import pygame

class Base:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, surface, camera_offset_x):
        # This method should be overridden by subclasses
        raise NotImplementedError("Subclasses must implement draw method.")