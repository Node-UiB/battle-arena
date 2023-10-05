"""
StaticSquare class
Obstacle in map, doesn't move and has inf mass

Inherits from:
    -> StaticSprite
        -> PolygonSprite
            -> pygame.sprite.Sprite

set_image_rect
"""

from Base.Mesh import Mesh
from Base.Transform import Transform
from Base.StaticSprite import StaticSprite


class Obstacle(StaticSprite):
    def __init__(self, mesh: Mesh, transform: Transform):
        super().__init__(mesh, transform)

    def set_image_rect(self):
        pass

