import numpy as np
from src.image.Image import Image
class ThermalImage (Image):
    def __init__(self, data: np.ndarray):
        super().__init__(data)
