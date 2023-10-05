"""
Wall

Inherits from:
    -> PolygonSprite
        -> pygame.sprite.Sprite
"""


from .PolygonSprite import PolygonSprite
from .Transform import Transform
from .Mesh import Mesh


class StaticSprite(PolygonSprite):
    def __init__(self, mesh: Mesh, transform: Transform):
        super().__init__(mesh, transform)

