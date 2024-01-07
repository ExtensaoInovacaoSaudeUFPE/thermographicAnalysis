import numpy as np
from src.image.types.RawImage import RawImage
class ThermalImage (RawImage):
    def __init__(self, data: np.ndarray, meta: dict[str, str] = None):
        super().__init__(data, meta)

    def getTemperatureAt(self, x: int, y: int) -> float:
        return float(self.data[y][x])


