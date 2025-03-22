# game_objects/__init__.py

from .game_object import GameObject
from .player import Player
from .enemy import Enemy
from .item import Item  # If you have an Item class

__all__ = ['GameObject', 'Player', 'Enemy', 'Item']  # Specifies what is exported when "import *" is used