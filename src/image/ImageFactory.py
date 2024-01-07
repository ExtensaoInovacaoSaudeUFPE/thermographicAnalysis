from abc import ABC, abstractmethod

from src.image.types.RawImage import RawImage
from src.image.types.RGBImage import RGBImage
from src.image.types.ThermalImage import ThermalImage

class ImageFactory(ABC):

    @staticmethod
    @abstractmethod
    def getRawImageFromPath(path: str) -> RawImage:
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