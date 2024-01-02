from dataclasses import dataclass

from src.image.Image import Image
from src.image.ImageFactory import ImageFactory
from src.image.RGBImage import RGBImage
from src.image.ThermalImage import ThermalImage

class HomeModel:
    def __init__(self, imageFactory: ImageFactory):
        self._imageFactory = imageFactory
        self._imageSelected = False
        self._currentFilePath = ""
        self._thermalImage: ThermalImage | None = None
        self._rgbImage: RGBImage | None = None
        self._rawImage: Image | None = None

    def getThermalImage(self) -> ThermalImage:
        return self._thermalImage

    def getRGBImage(self) -> RGBImage:
        return self._rgbImage

    def getRawImage(self) -> Image:
        return self._rawImage

    def importImage(self, path: str):
        possibleImage = self._imageFactory.getRawImageFromPath(path)

        if possibleImage is None:
            raise Exception("Invalid image")

        self._rawImage = possibleImage
        self._imageSelected = True
        self._currentFilePath = path
        self._rgbImage = None
        self._thermalImage = None

    def processThermalImage(self) -> None:
        if not self._imageSelected:
            raise Exception("No image selected")

        self._thermalImage = self._imageFactory.getThermalImageFromPath(self._currentFilePath)

    def processRGBImage(self) -> None:
        if not self._imageSelected:
            raise Exception("No image selected")

        self._rgbImage = self._imageFactory.getRGBImageFromPath(self._currentFilePath)