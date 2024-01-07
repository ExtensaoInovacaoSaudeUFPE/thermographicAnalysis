# import tkinter as tk
# import ttkbootstrap as ttk
import customtkinter as ctk
from PIL import Image

from src.gui.home.LoadedFrame import LoadedFrame
from src.gui.home.SearchFrame import SearchFrame
from src.gui.home.ThermalComparisonFrame import ThermalComparisonFrame
from src.gui.routing.FrameRouter import FrameRouter

WINDOW_TITLE = "Análise Termográfica"
START_GEOMETRY = "800x600"
HELP_NAME = "Ajuda"
HELP_MESSAGE = '''
e clicar no botão 'Ver Plot' para visualizar o gráfico de comparação termográfica.
Poderá ser feito zoom nas imagens a partir da lupa.
'''

class NavButton(ctk.CTkButton):
    def __init__(self, parent, text: str, image: ctk.CTkImage, command, **kwargs) -> None:
        super().__init__(parent, text=text, image=image, command=command, **kwargs)
        self.configure(border_spacing=10, fg_color="transparent", text_color=("gray10", "gray90"),
                       hover_color=("gray70", "gray30"), corner_radius=0, height=40, anchor="w")
class HomeWindow(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title(WINDOW_TITLE)
        self.geometry(START_GEOMETRY)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.setupIcons()
        self.setupContentFrame()
        self.setupNavigationFrame()


    def setupIcons(self) -> None:
        image_path = "static/icons/"
        self.logo_image = ctk.CTkImage(Image.open(image_path + "CustomTkinter_logo_single.png"), size=(26, 26))
        self.large_test_image = ctk.CTkImage(Image.open(image_path + "large_test_image.png"), size=(500, 150))
        self.image_icon_image = ctk.CTkImage(Image.open(image_path + "image_icon_light.png"), size=(20, 20))
        self.home_image = ctk.CTkImage(light_image=Image.open(image_path + "home_dark.png"),
                                       dark_image=Image.open(image_path + "home_light.png"), size=(20, 20))
        self.chat_image = ctk.CTkImage(light_image=Image.open(image_path + "chat_dark.png"),
                                       dark_image=Image.open(image_path + "chat_light.png"), size=(20, 20))
        self.add_user_image = ctk.CTkImage(light_image=Image.open(image_path + "add_user_dark.png"),
                                           dark_image=Image.open(image_path + "add_user_light.png"), size=(20, 20))

    def setupNavigationFrame(self) -> None:
        self.navigationFrame = ctk.CTkFrame(self)
        self.navigationFrame.grid(row=0, column=0, sticky="nsew")
        self.navigationFrame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigationFrame, text="   Análise Termográfica", image=self.logo_image,
                                                   compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = NavButton(self.navigationFrame, text="Home", image=self.home_image, command=lambda: self.routerFrame.switchScreen("search"))
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = NavButton(self.navigationFrame, text="Imagem Carregada", image=self.chat_image, command=lambda: self.routerFrame.switchScreen("loaded"))
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = NavButton(self.navigationFrame, text="Comparação Termográfica", image=self.add_user_image, command=lambda: self.routerFrame.switchScreen("comparison"))
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigationFrame, values=["Light", "Dark", "System"],
                                                      command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")


    def setupContentFrame(self) -> None:

        self.contentFrame = ctk.CTkFrame(self)
        self.contentFrame.grid(row=0, column=1, sticky="nsew")

        screens = {
            "search": SearchFrame(self.contentFrame),
            "loaded": LoadedFrame(self.contentFrame),
            "comparison": ThermalComparisonFrame(self.contentFrame)
        }

        self.routerFrame = FrameRouter()
        self.routerFrame.attachToScreens(screens)
        self.routerFrame.switchScreen("search")

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode) -> None:
        ctk.set_appearance_mode(new_appearance_mode)

