from src.image.ImageFactory import ImageFactory
from src.image.RGBImage import RGBImage
from src.image.ThermalImage import ThermalImage

from dependencies.FlirImageExtractor_master.flir_image_extractor import FlirImageExtractor

class FlirImageFactory(ImageFactory):
    exitool_path = r'dependencies\exiftool\exiftool.exe'

    @staticmethod
    def getRGBImageFromPath(path: str) -> RGBImage:
        flirImageExtractor = FlirImageExtractor(exiftool_path=FlirImageFactory.exitool_path)
        flirImageExtractor.process_image(path)

        return RGBImage(flirImageExtractor.extract_embedded_image())

    @staticmethod
    def getThermalImageFromPath(path: str) -> ThermalImage:
        flirImageExtractor = FlirImageExtractor(exiftool_path=FlirImageFactory.exitool_path)
        flirImageExtractor.process_image(path)

        return ThermalImage(flirImageExtractor.extract_thermal_image())