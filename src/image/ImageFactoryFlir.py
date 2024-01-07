from PIL import Image
import numpy as np

from src.image.types.RawImage import RawImage
from src.image.ImageFactory import ImageFactory
from src.image.types.RGBImage import RGBImage
from src.image.types.ThermalImage import ThermalImage

from dependencies.FlirImageExtractor_master.flir_image_extractor import FlirImageExtractor

class FlirImageFactory(ImageFactory):
    exitool_path = r'dependencies\exiftool\exiftool.exe'

    @staticmethod
    def getRawImageFromPath(path: str) -> RawImage:
        pil_image = Image.open(path)
        numpy_array = np.array(pil_image)

        return RawImage(numpy_array, {"path": path})


    @staticmethod
    def getRGBImageFromPath(path: str) -> RGBImage:
        flirImageExtractor = FlirImageExtractor(exiftool_path=FlirImageFactory.exitool_path)
        flirImageExtractor.process_image(path)

        return RGBImage(flirImageExtractor.extract_embedded_image(), {"path": path})

    @staticmethod
    def getThermalImageFromPath(path: str) -> ThermalImage:
        flirImageExtractor = FlirImageExtractor(exiftool_path=FlirImageFactory.exitool_path)
        flirImageExtractor.process_image(path)

        return ThermalImage(flirImageExtractor.extract_thermal_image(), {"path": path})

    @staticmethod
    def getRGBandThermalImageFromPath(path: str) -> (RGBImage, ThermalImage):
        flirImageExtractor = FlirImageExtractor(exiftool_path=FlirImageFactory.exitool_path)
        flirImageExtractor.process_image(path)

        return (RGBImage(flirImageExtractor.extract_embedded_image(), {"path": path}),
                ThermalImage(flirImageExtractor.extract_thermal_image(), {"path": path}))


