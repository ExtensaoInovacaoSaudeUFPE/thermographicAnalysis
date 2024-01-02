from typing import Protocol

import ttkbootstrap as ttk
import tkinter as tk
from tkinter import filedialog, messagebox
from src.gui.ThermalComparisonGraph import ThermalComparisonGraph
from src.gui.home.LoadedFrame import LoadedFrame
from src.gui.home.SearchFrame import SearchFrame
from src.image.ImageRaw import ImageRaw
from src.image.RGBImage import RGBImage
from src.image.ThermalImage import ThermalImage

WINDOW_TITLE = "Análise Termográfica"
START_GEOMETRY = "500x500"
HELP_NAME = "Ajuda"
HELP_MESSAGE = '''
e clicar no botão 'Ver Plot' para visualizar o gráfico de comparação termográfica.
Poderá ser feito zoom nas imagens a partir da lupa.
'''

class HomePresenter(Protocol):
    def importImageFromPath(self, path: str) -> None:
        ...

    def getImagesForComparison(self) -> tuple[RGBImage, ThermalImage] | None:
        ...

class HomeView:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.title(WINDOW_TITLE)
        self.window.geometry(START_GEOMETRY)
        self.presenter: HomePresenter | None = None

        self.screens = {
            "search": SearchFrame(self.window),
            "loaded": LoadedFrame(self.window)
        }

        self.screens["search"].bindSearchImageButton(self.searchImagePath)
        self.screens["loaded"].bindSearchAnotherImageButton(self.searchImagePath)
        self.screens["loaded"].bindThermalPlotButton(self.displayThermalComparisonGraph)

        self.currentScreen = "search"

    def initUI(self, presenter: HomePresenter) -> None:
        self.presenter = presenter
        self._setupMenu()
        self.currentScreen = "search"
        self.screens[self.currentScreen].pack(fill=tk.BOTH, expand=True)

    def _setupMenu(self) -> None:
        self.menu_bar = ttk.Menu(self.window)
        self.menu_bar.add_command(label=HELP_NAME, command=self._helpMessage)
        self.window.config(menu=self.menu_bar)

    def switchScreen(self, screen: str) -> None:
        if screen == self.currentScreen:
            return

        self.screens[self.currentScreen].pack_forget()
        self.currentScreen = screen
        self.screens[self.currentScreen].pack(fill=tk.BOTH, expand=True)

    def show(self) -> None:
        self.window.mainloop()

    def searchImagePath(self) -> None:
        path = filedialog.askopenfilename()
        self.presenter.importImageFromPath(path)

    def displayRawImage(self, image: ImageRaw) -> None:
        self.screens["loaded"].setImage(image)
        self.switchScreen("loaded")

    def displayThermalComparisonGraph(self) -> None:
        rgbImage, thermalImage = self.presenter.getImagesForComparison()
        ThermalComparisonGraph(rgbImage, thermalImage).plot()

    @staticmethod
    def showError(title: str, message: str) -> None:
        messagebox.showerror(title, message)

    @staticmethod
    def _helpMessage() -> None:
        messagebox.showinfo("Ajuda", HELP_MESSAGE)
