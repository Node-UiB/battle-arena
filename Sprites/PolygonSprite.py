import torch
import pygame

from Mesh import Mesh
from Transform import Transform
from Sprites.config import dtype, device

from typing import Optional


class PolygonSprite(pygame.sprite.Sprite):
    def __init__(self, mesh : Mesh, transform : Transform):
        self.mesh = mesh
        self.transform = transform

        self.UpdateImageRect()

    
    def UpdateImageRect(self):
        image = pygame.Surface((self.mesh.width, self.mesh.height), pygame.SRCALPHA)
        rotated_image = pygame.transform.rotate(image, -torch.rad2deg(self.transform.angle.item()))

        rotated_rect_center = self.transform.position + (self.transform.rotation_matrix @ (self.mesh.rect_center - self.mesh.center)[..., None])[..., 0]
        rotated_rect = rotated_image.get_rect(center=rotated_rect_center)

        self.image, self.rect = rotated_image, rotated_rect


    def UpdateTransformedVertices(self):
        self.transformed_vertices = self.transform.GetTransformedVertices(self.mesh)


    def update(self, 
               dt : float,
               new_position : Optional[torch.Tensor] = None,
               new_velocity : Optional[torch.Tensor] = None,
               new_acceleration : Optional[torch.Tensor] = None,
               new_angle : Optional[torch.Tensor] = None,
               new_angular_velocity : Optional[torch.Tensor] = None,
               new_angular_acceleration : Optional[torch.Tensor] = None):
        
        self.transform.update(dt, new_position, new_velocity, new_acceleration, new_angle, new_angular_velocity, new_angular_acceleration)

        self.UpdateImageRect()
        self.UpdateTransformedVertices()


if(__name__ == "__main__"):
    test_vertices = torch.as_tensor([[-100, -100], [100, -100], [100, 100], [-100, 100]], dtype=dtype, device=device)
    test_center = torch.as_tensor([0, 0], dtype=dtype, device=device)
    test_color = (255, 0, 0)

    test_mesh = Mesh(test_vertices, test_center, test_color)

    test_initial_position = torch.as_tensor([960, 540], dtype=dtype, device=device)
    test_initial_velocity = torch.as_tensor([0, 0], dtype=dtype, device=device)