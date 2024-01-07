from typing import Self

import numpy as np
from src.image.types.RawImage import RawImage
class RGBImage (RawImage):
    def __init__(self, data: np.ndarray, meta: dict[str, str] = None):
        super().__init__(data, meta)

    def crop(self, xmin: int, xmax: int, ymin: int, ymax: int) -> Self :
        return RGBImage(self.data[ymin:ymax, xmin:xmax])
