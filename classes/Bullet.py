import pygame
from pygame.math import Vector2
from Constants import Constants as con


class Bullet(pygame.sprite.Sprite):
    def __init__(
        self, start_x, start_y, dest_x, dest_y, size, speed, *sprite_groups
    ) -> None:
        super().__init__(*sprite_groups)
        self.image = pygame.Surface([size, size])
        self.image.fill(con.RED)
        self.image = pygame.transform.rotate(self.image, -angle)
        self.rect = self.image.get_rect(center=pos)

        offset = Vector2(80, 0).rotate(angle)

        self.pos = Vector2(pos) + offset
        self.velocity = Vector2(speed, 0)
        self.velocity.rotate_ip(angle)

        self.size = size
        self.speed = speed

    def update(self) -> None:
        self.pos += self.velocity
        self.rect.center = self.pos

        if self.rect.y > con.SCREEN_HEIGHT:
            self.kill()
        if self.rect.y < 0:
            self.kill()
        if self.rect.x > con.SCREEN_WIDTH:
            print("bullet killed")
            self.kill()
        if self.rect.x < 0:
            self.kill()
