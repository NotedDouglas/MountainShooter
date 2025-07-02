#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Tuple

from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.entity1 import Entity1


class Enemy(Entity1):
    def __init__(self, name: str, position: Tuple):
        super().__init__(name, position)
        pass

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        pass
