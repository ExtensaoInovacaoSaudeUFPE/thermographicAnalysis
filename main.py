
import os

script_dir = os.path.dirname(os.path.realpath(__file__))
print(script_dir)
os.chdir(script_dir)

from src.gui.home.HomeWindow import HomeWindow

def main() -> None:
    homeWindow = HomeWindow()
    homeWindow.show()


if __name__ == "__main__":
    main()