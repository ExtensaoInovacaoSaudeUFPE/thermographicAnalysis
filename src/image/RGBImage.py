import numpy as np
from src.image.Image import Image
class RGBImage (Image):
    def __init__(self, data: np.ndarray):
        super().__init__(data)

    def crop(self, xmin, xmax, ymin, ymax):
        return RGBImage(self.data[ymin:ymax, xmin:xmax])
