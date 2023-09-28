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