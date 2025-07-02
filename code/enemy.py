#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Tuple

from code.Const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SPEED_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.entity1 import Entity1


class Enemy(Entity1):
    def __init__(self, name: str, position: Tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SPEED_SHOT_DELAY[self.name]


    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SPEED_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
        return None