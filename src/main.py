from src.gui.Home import Home
import os

def main():
    home = Home()
    home.mainloop()

def setupPath():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    root_dir = os.path.dirname(script_dir)
    os.chdir(root_dir)


if __name__ == "__main__":
    setupPath()
    main()