from src.image.types.RawImage import RawImage
from src.image.types.RGBImage import RGBImage
from src.image.types.ThermalImage import ThermalImage


class ThermalImageBundle:
    raw: RawImage
    thermal: ThermalImage
    rgb: RGBImage

    def __init__(self, raw: RawImage, thermal: ThermalImage = None, rgb: RGBImage = None):
        self.raw = raw
        self.thermal = thermal
        self.rgb = rgb
