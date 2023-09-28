"""
Placeholder for original mesh vertices & center
"""
import torch as T

from typing import Tuple

class Mesh:
    def __init__(self, vertices : T.Tensor, center : T.Tensor, color : Tuple[int, int, int]):
        self.vertices = vertices
        self.center = center

        self.color = color


    def _FixBounds(self):
        B_0 = T.min(self.vertices).values

        self.vertices -= B_0
        self.center -= B_0

        dB = T.max(self.vertices).values

        self.width = dB[0].item()
        self.height = dB[1].item()