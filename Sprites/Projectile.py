"""
Projectile class
Spawned in with initial position & velocity and simulated entirely by pymunk

Inherits from:
    -> DynamicSprite
        -> PolygonSprite
            -> pygame.sprite.Sprite

update_image_rect
update
    -> Sets transform.position to body.position
"""


from Base.Mesh import Mesh
from Base.Transform import Transform
from Base.DynamicSprite import DynamicSprite


class Projectile(DynamicSprite):
    def __init__(self, mesh: Mesh, transform: Transform) -> None:
        super().__init__(mesh, transform)

    def update_image_rect(self):
        pass

    def update(self):
        pass
