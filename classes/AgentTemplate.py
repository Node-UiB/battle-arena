import math
import pygame
from pygame.math import Vector2
from Constants import Constants as con
from .Projectile import Projectile


class AgentTemplate(pygame.sprite.Sprite):
    def __init__(self, pos, rot, all_sprites, bullets) -> None:
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(con.BLACK)
        self.rect = self.image.get_rect()
        self.all_sprites = all_sprites
        self.add(self.all_sprites)
        self.bullets = bullets

        self.pos = pos
        self.speed = 0.1
        self.rot = rot
        self.rotspeed = 0.1
        self.size = 35

    def update(self):
        """Update position of player"""

        self.rect.center = pygame.mouse.get_pos()

        mouse_pressed = pygame.mouse.get_pressed()

        x, y = Vector2(pygame.mouse.get_pos()) - self.rect.center
        angle = math.degrees(math.atan2(y, x))

        if mouse_pressed[0]:
            Projectile(
                pygame.mouse.get_pos(), angle, 5, 0.1, self.all_sprites, self.bullets
            )
    def move(self, dir = 0):
        # passer på at dir ikke er mer enn 1 eller mindre enn -1
        dir = min(1, max(-1, dir))
        
        """ hvis vi trenger dette
        # beveger seg i retningen du ser og ikke går ut av rammen

        if self.size/2 <= self.pos[0] + sin(radians(self.rot))*self.speed*dir <= width-self.size/2:
            self.pos[0] += sin(radians(self.rot))*self.speed*dir
        if self.size/2 <= self.pos[1] + cos(radians(self.rot))*self.speed*dir <= height-self.size/2:
            self.pos[1] += cos(radians(self.rot))*self.speed*dir
        """
        # beveger seg i retningen du ser
        self.pos[0] += math.sin(math.radians(self.rot))*self.speed*dir
        self.pos[1] += math.cos(math.radians(self.rot))*self.speed*dir
    
    def rotate(self, dir = 1):
        # passer på at dir ikke er mer enn 1 eller mindre enn -1
        dir = min(1, max(-1, dir))

        self.rot = (self.rot+dir*self.rotspeed)%360

    def shoot(self):
        print("pew")
