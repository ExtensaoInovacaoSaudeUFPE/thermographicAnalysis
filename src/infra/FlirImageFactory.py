from src.model.Image import Image
from src.model.ImageFactory import ImageFactory
from src.model.ThermalImage import ThermalImage

from dependencies.FlirImageExtractor_master.flir_image_extractor import FlirImageExtractor

class FlirImageFactory(ImageFactory):
    exitool_path = 'dependencies/flir_image_extractor/exiftool.exe'

    @staticmethod
    def getRawImageFromPath(path: str) -> Image:
        flirImageExtractor = FlirImageExtractor(exiftool_path=FlirImageFactory.exitool_path)
        flirImageExtractor.process_image(path)

        return Image(flirImageExtractor.extract_embedded_image())

    @staticmethod
    def getThermalImageFromPath(path: str) -> ThermalImage:
        flirImageExtractor = FlirImageExtractor(exiftool_path=FlirImageFactory.exitool_path)
        flirImageExtractor.process_image(path)

        return ThermalImage(flirImageExtractor.extract_thermal_image())