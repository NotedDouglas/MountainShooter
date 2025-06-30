from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.entity1 import Entity1

class Background(Entity1):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        pass
