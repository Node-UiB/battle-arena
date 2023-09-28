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