from src.gui.ThermalComparisonGraph import ThermalComparisonGraph
from src.infra.FlirImageFactory import FlirImageFactory
import os

def main():

    imagePath = r'test\images\FLIR0676.jpg'
    rgbImage = FlirImageFactory.getRGBImageFromPath(imagePath)
    thermalImage = FlirImageFactory.getThermalImageFromPath(imagePath)
    ThermalComparisonGraph(rgbImage, thermalImage).plot()

def setupPath():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.dirname(script_dir)
    os.chdir(root_dir)
    print("Current working directory:", os.getcwd())

if __name__ == "__main__":
    setupPath()
    main()