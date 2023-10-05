"""
Agent class

Inherits from:
    -> KinematicSprite
        -> PolygonSprite
            -> pygame.sprite.Sprite

update_image_rect
update_rays
update
shoot
"""

from Base.Mesh import Mesh
from Base.Transform import Transform
from Base.KinematicSprite import KinematicSprite


class Agent(KinematicSprite):
    def __init__(self, mesh: Mesh, transform: Transform) -> None:
        super().__init__(mesh, transform)

    def update(self):
        pass

    def update_image_rect(self):
        pass

    def update_rays(self):
        pass

    def shoot(self):
        pass
