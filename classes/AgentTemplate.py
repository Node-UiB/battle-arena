import math
import pygame
from pygame.math import Vector2
from Constants import Constants as con
from .Projectile import Projectile


class AgentTemplate(pygame.sprite.Sprite):
    def __init__(self, pos, all_sprites, bullets) -> None:
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(con.BLACK)
        self.rect = self.image.get_rect()
        self.all_sprites = all_sprites
        self.add(self.all_sprites)
        self.bullets = bullets

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

    def shoot(self):
        print("pew")
