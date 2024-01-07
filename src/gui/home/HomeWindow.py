import tkinter as tk
import ttkbootstrap as ttk
from src.gui.home.LoadedFrame import LoadedFrame
from src.gui.home.SearchFrame import SearchFrame
from src.gui.home.ThermalComparisonFrame import ThermalComparisonFrame
from src.gui.routing.FrameRouter import FrameRouter

WINDOW_TITLE = "Análise Termográfica"
START_GEOMETRY = "500x500"
HELP_NAME = "Ajuda"
HELP_MESSAGE = '''
e clicar no botão 'Ver Plot' para visualizar o gráfico de comparação termográfica.
Poderá ser feito zoom nas imagens a partir da lupa.
'''

class HomeWindow:
    def __init__(self) -> None:
        self.window = ttk.Window()
        self.window.title(WINDOW_TITLE)
        self.window.geometry(START_GEOMETRY)
        self.window.config(background="red")


        self.contentFrame = tk.Frame()
        self.contentFrame.pack(fill=tk.BOTH, expand=True)
        screens = {
            "search": SearchFrame(self.contentFrame),
            "loaded": LoadedFrame(self.contentFrame),
            "comparison": ThermalComparisonFrame(self.contentFrame)
        }
        self.routerFrame = FrameRouter()
        self.routerFrame.attachToScreens(screens)
        self.routerFrame.switchScreen("search")

    def show(self) -> None:
        self.window.mainloop()
