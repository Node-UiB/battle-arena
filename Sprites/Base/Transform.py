import torch

from .Mesh import Mesh

# from .config import dtype, device
from .Config import Config
from typing import Optional

dtype = Config.dtype
device = Config.device


class Transform:
    def __init__(
        self,
        initial_position: Optional[torch.Tensor] = None,
        initial_velocity: Optional[torch.Tensor] = None,
        initial_acceleration: Optional[torch.Tensor] = None,
        initial_angle: Optional[torch.Tensor] = None,
        initial_angular_velocity: Optional[torch.Tensor] = None,
        initial_angular_acceleration: Optional[torch.Tensor] = None,
        static: bool = False,
    ):
        self.position = (
            initial_position
            if initial_position is not None
            else torch.as_tensor([0, 0], dtype=dtype, device=device)
        )
        self.velocity = (
            initial_velocity
            if initial_velocity is not None
            else torch.as_tensor([0, 0], dtype=dtype, device=device)
        )
        self.acceleration = (
            initial_acceleration
            if initial_acceleration is not None
            else torch.as_tensor([0, 0], dtype=dtype, device=device)
        )

        self.angle = (
            initial_angle
            if initial_angle is not None
            else torch.as_tensor(0, dtype=dtype, device=device)
        )
        self.angular_velocity = (
            initial_angular_velocity
            if initial_angular_velocity is not None
            else torch.as_tensor(0, dtype=dtype, device=device)
        )
        self.angular_acceleration = (
            initial_angular_acceleration
            if initial_angular_acceleration is not None
            else torch.as_tensor(0, dtype=dtype, device=device)
        )

        self.static = static

        self._UpdateRotationMatrix()

    def _UpdateRotationMatrix(self):
        c, s = torch.cos(self.angle), torch.sin(self.angle)
        self.rotation_matrix = torch.stack((c, -s, s, c), dim=0).view(2, 2)

    def update(
        self,
        dt: float,
        new_position: Optional[torch.Tensor] = None,
        new_velocity: Optional[torch.Tensor] = None,
        new_acceleration: Optional[torch.Tensor] = None,
        new_angle: Optional[torch.Tensor] = None,
        new_angular_velocity: Optional[torch.Tensor] = None,
        new_angular_acceleration: Optional[torch.Tensor] = None,
    ):
        if self.static:
            return

        if new_acceleration is not None:
            self.acceleration = new_acceleration

        if new_velocity is not None:
            self.velocity = new_velocity
        else:
            self.velocity += self.acceleration * dt

        if new_position is not None:
            self.position = new_position
        else:
            self.position += self.velocity * dt

        if new_angular_acceleration is not None:
            self.angular_acceleration = new_angular_acceleration

        if new_angular_velocity is not None:
            self.angular_velocity = new_angular_velocity
        else:
            self.angular_velocity += self.angular_acceleration * dt

        if new_angle is not None:
            self.angle = new_angle
        else:
            self.angle += self.angular_velocity * dt

        self._UpdateRotationMatrix()

    def GetTransformedVertices(self, mesh: Mesh) -> torch.Tensor:
        return (self.rotation_matrix @ (mesh.vertices - mesh.center)[..., None])[
            ..., 0
        ] + self.position
