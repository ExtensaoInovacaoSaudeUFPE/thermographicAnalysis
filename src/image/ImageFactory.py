from abc import ABC, abstractmethod

from src.image.RGBImage import RGBImage
from src.image.ThermalImage import ThermalImage

class ImageFactory(ABC):
    def __init__(self, image_path):
        self.image_path = image_path

    @staticmethod
    @abstractmethod
    def getRGBImageFromPath(path: str) -> RGBImage:
        pass

    @staticmethod
    @abstractmethod
    def getThermalImageFromPath(path: str) -> ThermalImage:
        pass