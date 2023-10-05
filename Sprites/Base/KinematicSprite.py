"""
Player & gun

Inherits from:
    -> PolygonSprite
        -> pygame.sprite.Sprite

update : dt, force, torque -> None
    Updates internal transfrom
    Sets internal bodys state to transforms state
"""

from .PolygonSprite import PolygonSprite
from .Transform import Transform
from .Mesh import Mesh


class KinematicSprite(PolygonSprite):
    def __init__(self, mesh: Mesh, transform: Transform) -> None:
        super().__init__(mesh, transform)

    def update(self, dt, force, torque) -> None:
        pass

