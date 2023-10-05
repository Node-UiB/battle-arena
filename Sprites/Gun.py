"""
Gun class

width, height, parent, angle_offset

parent.transfrom.angle + angle_offset

Inherits from:
    -> KinematicSprite
        -> PolygonSprite
            -> pygame.sprite.Sprite

shoot

update_image_rect

update
    -> Follows parent agents position & rotation
"""

from Base.Transform import Transform
from Base.KinematicSprite import KinematicSprite
from Base.Mesh import Mesh


class Gun(KinematicSprite):
    def __init__(
        self, width, height, parent, angle_offset, mesh: Mesh, transform: Transform
    ) -> None:
        super().__init__(mesh, transform)

    def shoot(self):
        pass

    def update(self):
        pass

    def update_image_rect(self):
        pass

