from src.image.ImageFactory import ImageFactory
from src.image.ImageFactoryFlir import FlirImageFactory
from src.image.ImageRepository import ImageRepository
from src.image.types.RGBImage import RGBImage
from src.image.types.RawImage import RawImage
from src.image.types.ThermalImage import ThermalImage
from src.image.types.ThermalImageBundle import ThermalImageBundle


class ImageService:
    def __init__(self, imageFactory: ImageFactory, imageRepository: ImageRepository):
        self._imageFactory = imageFactory
        self._imageRepository = imageRepository

    def getThermalImage(self, id: str) -> ThermalImage:
        bundle = self._imageRepository.getThermalImageBundleById(id)
        if bundle is None:
            raise Exception("Record Doesnt exist")

        if bundle.thermal is None:
            raise Exception("Thermal Image not processed")

        return bundle.thermal

    def getRGBImage(self, id: str) -> RGBImage:
        bundle = self._imageRepository.getThermalImageBundleById(id)
        if bundle is None:
            raise Exception("Record Doesnt exist")

        if bundle.rgb is None:
            raise Exception("RGB Image not processed")
        return bundle.rgb

    def getRawImage(self, id: str) -> RawImage:
        bundle = self._imageRepository.getThermalImageBundleById(id)
        if bundle is None:
            raise Exception("Record Doesnt exist")

        if bundle.raw is None:
            raise Exception("Raw Image not processed")

        return bundle.raw

    def importImage(self, path: str, id: str) -> None:
        possibleImage = self._imageFactory.getRawImageFromPath(path)
        if possibleImage is None:
            raise Exception("Invalid image")

        self._imageRepository.insertImageBundle(ThermalImageBundle(possibleImage), id)

    def deleteImage(self, id: str) -> None:
        try:
            self._imageRepository.deleteThermalImageBundleById(id)
        except Exception as e:
            raise Exception("Record Doesnt exist")

    def processRGBandThermalImages(self, id: str) -> None:
        bundle = self._imageRepository.getThermalImageBundleById(id)
        if bundle is None or bundle.raw is None:
            raise Exception("Record Doesnt exist")
        elif bundle.thermal is None or bundle.rgb is None:
            try:
                rgbImage, thermalImage = self._imageFactory.getRGBandThermalImageFromPath(bundle.raw.meta["path"])
            except Exception as e:
                raise Exception("Error processing image")

            self._imageRepository.updateThermalImageBundleById(id, ThermalImageBundle(bundle.raw, thermalImage, rgbImage))


imageService = ImageService(FlirImageFactory(), ImageRepository())