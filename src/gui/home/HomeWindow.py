import customtkinter as ctk
from PIL import Image

from src.gui.home.CommentFrame import CommentFrame
from src.gui.home.LoadedFrame import LoadedFrame
from src.gui.home.SearchFrame import SearchFrame
from src.gui.home.ThermalComparisonFrame import ThermalComparisonFrame
from src.gui.navBar.NavFrame import NavFrame
from src.gui.routing.FrameRouter import FrameRouter

WINDOW_TITLE = "Análise Termográfica"
START_GEOMETRY = "800x600"
HELP_NAME = "Ajuda"
HELP_MESSAGE = '''
e clicar no botão 'Ver Plot' para visualizar o gráfico de comparação termográfica.
Poderá ser feito zoom nas imagens a partir da lupa.
'''


class HomeWindow(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title(WINDOW_TITLE)
        self.geometry(START_GEOMETRY)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.setupContentFrame()
        self.setupNavigationFrame()

    def setupContentFrame(self) -> None:

        self.contentFrame = ctk.CTkFrame(self)
        self.contentFrame.grid(row=0, column=1, sticky="nsew")

        screens = {
            "search": SearchFrame(self.contentFrame),
            "loaded": LoadedFrame(self.contentFrame),
            "comparison": ThermalComparisonFrame(self.contentFrame),
            "comments": CommentFrame(self.contentFrame)
        }

        self.routerFrame = FrameRouter()
        self.routerFrame.attachToScreens(screens)
        self.routerFrame.switchScreen("search")
        
    def setupNavigationFrame(self) -> None:
        self.navigationFrame = NavFrame(self)
        self.navigationFrame.grid(row=0, column=0, sticky="nsew")
        self.navigationFrame.setRouter(self.routerFrame)



