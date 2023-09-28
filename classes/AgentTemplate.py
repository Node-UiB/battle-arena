import pygame
from Constants import Constants as con
from .Projectile import Projectile


class AgentTemplate(pygame.sprite.Sprite):
    def __init__(self, position, all_sprites, bullets) -> None:
        super().__init__()
        self.position = position
        self.image = pygame.Surface([20, 20])
        self.image.fill(con.BLACK)
        self.rect = self.image.get_rect()
        self.all_sprites = all_sprites
        self.add(self.all_sprites)
        self.bullets = bullets

    def update(self):
        """Update position of player"""

        # self.rect.center = pygame.mouse.get_pos()

    def shoot(self):
        mouse_pressed = pygame.mouse.get_pressed()

        x, y = pygame.mouse.get_pos()

        if mouse_pressed[0]:
            Projectile(
                self.rect.center[0], self.rect.center[1], x, y, 100, 5, self.bullets
            )
        print("pew")
