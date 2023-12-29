import numpy as np
from src.model.Image import Image
class ThermalImage (Image):
    def __init__(self, data: np.ndarray):
        super().__init__(data)
