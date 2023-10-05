import torch
import pygame

from Mesh import Mesh
from Transform import Transform
from config import dtype, device

from typing import Optional


class PolygonSprite(pygame.sprite.Sprite):
    def __init__(self, mesh : Mesh, transform : Transform):
        self.mesh = mesh
        self.transform = transform

        self.UpdateImageRect()
        self.UpdateTransformedVertices()

    
    def UpdateImageRect(self):
        image = pygame.Surface((self.mesh.width, self.mesh.height), pygame.SRCALPHA)
        pygame.draw.polygon(image, self.mesh.color, self.mesh.vertices.cpu().numpy())
        rotated_image = pygame.transform.rotate(image, -torch.rad2deg(self.transform.angle).item())

        rotated_rect_center = self.transform.position + (self.transform.rotation_matrix @ (self.mesh.rect_center - self.mesh.center)[..., None])[..., 0]
        rotated_rect = rotated_image.get_rect(center=rotated_rect_center.cpu().numpy())

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
    import sys
    from time import time

    test_vertices = torch.as_tensor([[-100, -100], [100, -100], [100, 100], [-100, 100]], dtype=dtype, device=device)
    test_center = torch.as_tensor([100, 0], dtype=dtype, device=device)
    test_color = (0, 255, 0)

    test_mesh = Mesh(test_vertices, test_center, test_color)

    test_initial_position = torch.as_tensor([0, 540], dtype=dtype, device=device)
    test_initial_acceleration = torch.as_tensor([50, 0], dtype=dtype, device=device)
    test_initial_angular_velocity = torch.as_tensor(0.5 * torch.pi, dtype=dtype, device=device)

    test_transform = Transform(initial_position=test_initial_position, initial_acceleration=test_initial_acceleration, initial_angular_velocity=test_initial_angular_velocity)

    test_polygon_sprite = PolygonSprite(test_mesh, test_transform)


    pygame.init()

    screen = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

    running = True
    while(running == True):
        t0 = time()
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                running == False

        screen.fill((255, 0, 0))
        screen.blit(test_polygon_sprite.image, test_polygon_sprite.rect)

        transformed_test_vertices = test_polygon_sprite.transformed_vertices.cpu().numpy()
        for i in range(4):
            pygame.draw.circle(screen, (255, 255, 255), transformed_test_vertices[i], 5)

        pygame.draw.circle(screen, (0, 0, 0), test_polygon_sprite.transform.position.cpu().numpy(), 10)

        pygame.display.flip()

        tf = time()
        dt = tf - t0

        test_polygon_sprite.update(dt)

    pygame.quit()
    sys.exit()