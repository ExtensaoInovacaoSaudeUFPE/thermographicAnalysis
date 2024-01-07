from typing import Self
from PIL import Image, ImageTk
import numpy as np
from abc import ABC
class RawImage(ABC):
    data: np.ndarray
    meta: dict[str, str] = {}

    def __init__(self, data: np.ndarray, meta: dict[str, str] = None):
        self.data = data
        self.meta = meta

    def crop(self, xmin, xmax, ymin, ymax) -> Self:
        return RawImage(self.data[ymin:ymax, xmin:xmax])

    def toTkImage(self, maxSize: tuple[int, int] | None = None) -> ImageTk.PhotoImage:
        image = Image.fromarray(self.data)
        if maxSize:
            image.thumbnail(maxSize)
        return ImageTk.PhotoImage(image)
