# entities/base.py

class BaseEntity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update(self):
        pass

    def draw(self, surface):
        pass