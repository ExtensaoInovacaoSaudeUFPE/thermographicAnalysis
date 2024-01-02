from __future__ import annotations

from typing import Protocol

from src.gui.home.HomeModel import HomeModel
from src.image.ImageRaw import ImageRaw
from src.image.RGBImage import RGBImage
from src.image.ThermalImage import ThermalImage


class HomeView(Protocol):
    def initUI(self, presenter: HomePresenter):
        ...

    def show(self) -> None:
        ...

    def displayRawImage(self, image: ImageRaw) -> None:
        ...

    def showError(self, title: str, message: str) -> None:
        ...

class HomePresenter:
    def __init__(self, model: HomeModel, view: HomeView):
        self.model = model
        self.view = view

    def start(self) -> None:
        self.view.initUI(self)
        self.view.show()

    def importImageFromPath(self, path: str) -> None:
        print(path)
        try:
            self.model.importImage(path)
        except Exception as e:
            print(e)
            self.view.showError("Erro", "Erro ao importar imagem")
            return

        self.view.displayRawImage(self.model.getRawImage())

    def getImagesForComparison(self) -> tuple[RGBImage, ThermalImage] | None:
        try:
            self.model.processRGBandThermalImages()
        except Exception as e:
            print(e)
            self.view.showError("Erro", "Erro ao processar imagem")
            return

        rgbImage = self.model.getRGBImage()
        thermalImage = self.model.getThermalImage()

        return rgbImage, thermalImage


