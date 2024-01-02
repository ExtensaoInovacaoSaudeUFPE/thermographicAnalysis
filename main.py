
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
print(script_dir)
os.chdir(script_dir)


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


if __name__ == "__main__":
    main()