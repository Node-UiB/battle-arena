"""
Projectile

Inherits from:
    -> PolygonSprite
        -> pygame.sprite.Sprite

update : dt -> None
    Updates internal transfrom
"""

from .PolygonSprite import PolygonSprite
from .Mesh import Mesh
from .Transform import Transform


class DynamicSprite(PolygonSprite):
    def __init__(self, mesh: Mesh, transform: Transform) -> None:
        super().__init__(mesh, transform)

    def update(self, dt) -> None:
        pass
