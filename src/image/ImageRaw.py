from typing import Self
from PIL import Image, ImageTk
import numpy as np
from abc import ABC
class ImageRaw(ABC):
    data: np.ndarray

    def __init__(self, data: np.ndarray):
        self.data = data

    def crop(self, xmin, xmax, ymin, ymax) -> Self:
        return ImageRaw(self.data[ymin:ymax, xmin:xmax])

    def toTkImage(self, maxSize: tuple[int, int] | None = None) -> ImageTk.PhotoImage:
        image = Image.fromarray(self.data)
        if maxSize:
            image.thumbnail(maxSize)
        return ImageTk.PhotoImage(image)
