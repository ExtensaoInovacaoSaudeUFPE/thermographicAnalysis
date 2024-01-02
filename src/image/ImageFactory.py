from abc import ABC, abstractmethod

from src.image.ImageRaw import ImageRaw
from src.image.RGBImage import RGBImage
from src.image.ThermalImage import ThermalImage

class ImageFactory(ABC):

    @staticmethod
    @abstractmethod
    def getRawImageFromPath(path: str) -> ImageRaw:
        pass

    @staticmethod
    @abstractmethod
    def getRGBImageFromPath(path: str) -> RGBImage:
        pass

    @staticmethod
    @abstractmethod
    def getThermalImageFromPath(path: str) -> ThermalImage:
        pass

    @staticmethod
    @abstractmethod
    def getRGBandThermalImageFromPath(path: str) -> (RGBImage, ThermalImage):
        pass