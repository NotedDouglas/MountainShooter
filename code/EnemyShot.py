from code.Const import ENTITY_SPEED
from code.entity1 import Entity1


class EnemyShot(Entity1):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]