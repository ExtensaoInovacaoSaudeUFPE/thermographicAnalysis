from abc import ABC, abstractmethod

from src.model.Image import Image
from src.model.ThermalImage import ThermalImage

class ImageFactory(ABC):
    def __init__(self, image_path):
        self.image_path = image_path

    @staticmethod
    @abstractmethod
    def getRawImageFromPath(path: str) -> Image:
        pass

    @staticmethod
    @abstractmethod
    def getThermalImageFromPath(path: str) -> ThermalImage:
        pass