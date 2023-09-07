import pygame
from Constants import Constants as con


class PlayerTemplate(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill(con.BLACK)
        self.rect = self.image.get_rect()

    def update(self):
        """Update position of player"""
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
