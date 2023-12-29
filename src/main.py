from src.gui.ThermalComparisonGraph import ThermalComparisonGraph
from src.infra.FlirImageFactory import FlirImageFactory


def main():
    imagePath = r'C:\\Users\\igor_\\Documents\\dev\\ufpe\\extensaoColaborativa\\Novas_imagens\\FLIR0686.jpg'
    rgbImage = FlirImageFactory.getRGBImageFromPath(imagePath)
    thermalImage = FlirImageFactory.getThermalImageFromPath(imagePath)

    thermalComparisonGraph = ThermalComparisonGraph(rgbImage, thermalImage)
    thermalComparisonGraph.plot()

if __name__ == "__main__":
    main()