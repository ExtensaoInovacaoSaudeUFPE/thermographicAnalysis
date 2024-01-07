from src.image.types.ThermalImageBundle import ThermalImageBundle

class ImageRepository:
    data: dict[str, ThermalImageBundle] = {}

    def insertImageBundle(self, imageBundle: ThermalImageBundle, id: str) -> None:
        self.data[id] = imageBundle

    def getThermalImageBundleById(self, id: str) -> ThermalImageBundle | None:
        if id not in self.data:
            return None
        return self.data[id]

    def getAllThermalImageBundles(self) -> dict[str, ThermalImageBundle]:
        return self.data

    def deleteThermalImageBundleById(self, id: str) -> None:
        if id not in self.data:
            raise Exception("Image with id " + id + " does not exist")

        if id in self.data:
            del self.data[id]

    def updateThermalImageBundleById(self, id: str, imageBundle: ThermalImageBundle) -> None:
        if id in self.data:
            self.data[id] = imageBundle