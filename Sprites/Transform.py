"""
Transform class

Keeps track of sprite:
    position
    velocity
    acceleration

    angle
    angular_velocity
    angular_acceleration
"""


import torch as T

from typing import Optional


class Transform:
    def __init__(self,
                 initial_position : Optional[T.Tensor] = None,
                 initial_velocity : Optional[T.Tensor] = None,
                 initial_acceleration : Optional[T.Tensor] = None,
                 initial_angle : Optional[T.Tensor] = None,
                 initial_angular_velocity : Optional[T.Tensor] = None,
                 initial_angular_acceleration : Optional[T.Tensor] = None,
                 static : bool = False):
        
        set attr


    update -> dt ->
        if static
            return


    transform : mesh -> vertices
        