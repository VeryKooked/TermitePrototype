# general game objects

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self, surface):
        pass  # This will be implemented in subclasses