import numpy as np
from src.image.ImageRaw import ImageRaw
class ThermalImage (ImageRaw):
    def __init__(self, data: np.ndarray):
        super().__init__(data)

    def getTemperatureAt(self, x: int, y: int) -> float:
        return float(self.data[y][x])


