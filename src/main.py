import os

from src.gui.home.HomeModel import HomeModel
from src.gui.home.HomePresenter import HomePresenter
from src.gui.home.HomeView import HomeView
from src.infra.FlirImageFactory import FlirImageFactory


def main() -> None:
    imageFactory = FlirImageFactory()
    model = HomeModel(imageFactory)
    view = HomeView()
    home = HomePresenter(model, view)
    home.start()

def setupPath() -> None:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.dirname(script_dir)
    os.chdir(root_dir)


if __name__ == "__main__":
    setupPath()
    main()