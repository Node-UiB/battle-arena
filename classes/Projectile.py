import pygame
from Constants import Constants as con


class Projectile(pygame.sprite.Sprite):
    def __init__(self, *groups, size, speed, **kwargs) -> None:
        super().__init__(*groups, **kwargs)
        self.image = pygame.Surface([size, size])
        self.image.fill(con.RED)
        self.rect = self.image.get_rect()

        self.size = size
        self.speed = speed
