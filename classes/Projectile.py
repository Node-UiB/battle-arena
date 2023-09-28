import pygame
import math
from pygame.math import Vector2
from Constants import Constants as con


class Projectile(pygame.sprite.Sprite):
    def __init__(
        self, start_x, start_y, dest_x, dest_y, size, speed, *sprite_groups
    ) -> None:
        super().__init__(*sprite_groups)

        self.position = (start_x, start_y)
        self.speed = speed
        self.direction = (dest_x - start_x, dest_y - start_y)

        # Normalizing vector
        length = math.hypot(*self.direction)
        if length == 0.0:
            self.direction = (0, -1)
        else:
            self.direction = (self.direction[0] / length, self.direction[1] / length)

        angle = math.degrees(math.atan2(-self.direction[1], self.direction[0]))

        self.image = pygame.Surface([size, size]).convert_alpha()
        self.image.fill(con.RED)
        self.image = pygame.transform.rotate(self.image, angle)


        self.rect = self.image.get_rect(center=self.position)

    def update(self) -> None:
        self.position = (self.position[0]+self.direction[0]*self.speed,
                         self.position[0]+self.direction[0]*self.speed)

        if self.rect.y > con.SCREEN_HEIGHT:
            self.kill()
        if self.rect.y < 0:
            self.kill()
        if self.rect.x > con.SCREEN_WIDTH:
            print("bullet killed")
            self.kill()
        if self.rect.x < 0:
            self.kill()
