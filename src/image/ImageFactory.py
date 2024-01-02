from abc import ABC, abstractmethod

from src.image.Image import Image
from src.image.RGBImage import RGBImage
from src.image.ThermalImage import ThermalImage

class ImageFactory(ABC):

    @staticmethod
    @abstractmethod
    def getRawImageFromPath(path: str) -> Image:
        pass

    @staticmethod
    @abstractmethod
    def getRGBImageFromPath(path: str) -> RGBImage:
        pass

    @staticmethod
    @abstractmethod
    def getThermalImageFromPath(path: str) -> ThermalImage:
        pass