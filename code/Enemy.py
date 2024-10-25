#!/usr/bin/python
# -*- coding: utf-8 -*-


from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT, VERTICAL_SPEED
from code.EnemyShot import EnemyShot
from code.Entity import Entity



class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.name == 'Enemy3': # Dúvido alguém resolver esse com mais gambiarra!
            if self.speed<0 and self.rect.centery<10:
                self.speed = 1
            elif self.speed>=0 and self.rect.centery> WIN_HEIGHT-10:
                self.speed = -1
            if self.speed >= 0:
                self.rect.centery += 2*VERTICAL_SPEED
            else:
                self.rect.centery -= VERTICAL_SPEED




    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

