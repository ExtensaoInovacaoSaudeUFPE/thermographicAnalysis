import os

from src.gui.ThermalComparisonGraph import ThermalComparisonGraph
from src.infra.FlirImageFactory import FlirImageFactory


def manualTest():
    imagePath = r'test\images\FLIR0676.jpg'
    imagePath =  r"C:\Users\igor_\Documents\dev\ufpe\extensaoColaborativa\Novas_imagens\FLIR0674.jpg"
    rgbImage = FlirImageFactory.getRGBImageFromPath(imagePath)
    thermalImage = FlirImageFactory.getThermalImageFromPath(imagePath)
    ThermalComparisonGraph(rgbImage, thermalImage).plot()

def setupPath():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.dirname(script_dir)
    os.chdir(root_dir)


if __name__ == "__main__":
    setupPath()
    manualTest()