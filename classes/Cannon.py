import pygame
from Constants import Constants as con
from .Projectile import Projectile


class Cannon(pygame.sprite.Sprite):
    def __init__(self, x, y, *sprite_groups) -> None:
        super().__init__()
        self.image = pygame.Surface([])

    def update(self) -> None:
        return
