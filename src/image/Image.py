from typing import Self
from PIL import (Image as Pil_Image, ImageTk)
import numpy as np
from abc import ABC
class Image(ABC):
    data: np.ndarray

    def __init__(self, data: np.ndarray):
        self.data = data

    def crop(self, xmin, xmax, ymin, ymax) -> Self:
        return Image(self.data[ymin:ymax, xmin:xmax])

    def toTkImage(self, maxSize: tuple[int, int] | None = None) -> ImageTk.PhotoImage:
        image = Pil_Image.fromarray(self.data)
        if maxSize:
            image.thumbnail(maxSize)
        return ImageTk.PhotoImage(image)
