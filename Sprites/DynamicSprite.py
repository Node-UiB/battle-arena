"""
Projectile

Inherits from:
    -> PolygonSprite
        -> pygame.sprite.Sprite

update : dt -> None
    Updates internal transfrom
"""

from Sprites.PolygonSprite import PolygonSprite


class DynamicSprite(PolygonSprite):
    def __init__(self) -> None:
        super().__init__()

    def update(self, dt) -> None:
        pass
