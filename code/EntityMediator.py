from code import player
from code.Const import WIN_WIDTH
from code.EnemyShot import EnemyShot
from code.PlayerShot import PlayerShot
from code.enemy import Enemy
from code.entity1 import Entity1
from code.player import Player


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity1):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
            if isinstance(ent, PlayerShot):
                if ent.rect.left >= WIN_WIDTH:
                    ent.health = 0
            if isinstance(ent, EnemyShot):
                if ent.rect.right <= 0:
                    ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent_one, ent_two):
        valid_interaction = False
        if isinstance(ent_one, Enemy) and isinstance(ent_two, PlayerShot):
            valid_interaction = True
        elif isinstance(ent_one, PlayerShot) and isinstance(ent_two, Enemy):
            valid_interaction = True
        elif isinstance(ent_one, Player) and isinstance(ent_two, EnemyShot):
            valid_interaction = True
        elif isinstance(ent_one, EnemyShot) and isinstance(ent_two, Player):
            valid_interaction = True

        if valid_interaction == True:
            if (ent_one.rect.right >= ent_two.rect.left and
                    ent_one.rect.left <= ent_two.rect.right and
                    ent_one.rect.bottom >= ent_two.rect.top and
                    ent_one.rect.top <= ent_two.rect.bottom):
                ent_one.health -= ent_two.damage
                ent_two.health -= ent_one.damage
                ent_one.last_dmg = ent_two.name
                ent_two.last_dmg = ent_one.name

    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity1]):
        if enemy.last_dmg == 'Player1Shot':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Player2Shot':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def verify_collision(entity_list: list[Entity1]):
        for i in range(len(entity_list)):
            entity_one = entity_list[i]
            EntityMediator.__verify_collision_window(entity_one)
            for j in range(i + 1, len(entity_list)):
                entity_two = entity_list[j]
                EntityMediator.__verify_collision_entity(entity_one, entity_two)

    @staticmethod
    def verify_health(entity_list: list[Entity1]):
        for ent in entity_list:
            if ent.health <= 0:
                if isinstance(ent, Enemy):
                    EntityMediator.__give_score(ent, entity_list)
                entity_list.remove(ent)
