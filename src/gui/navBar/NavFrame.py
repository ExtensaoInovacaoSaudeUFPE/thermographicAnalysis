import customtkinter as ctk
from PIL import Image

from src.gui.navBar.NavButton import NavButton
from src.gui.routing.FrameRouter import FrameRouter


class NavFrame(ctk.CTkFrame):
    router: FrameRouter

    def __init__(self, master) -> None:
        super().__init__(master)
        self.setupIcons()
        self.setupNavigationFrame()

    def setRouter(self, router) -> None:
        self.router = router

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

        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self, text="   Análise Termográfica", image=self.logo_image,
                                                   compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = NavButton(self, text="Home", image=self.home_image, command=lambda: self.router.switchScreen("search"))
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = NavButton(self, text="Imagem Carregada", image=self.chat_image, command=lambda: self.router.switchScreen("loaded"))
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = NavButton(self, text="Comparação Termográfica", image=self.add_user_image, command=lambda: self.router.switchScreen("comparison"))
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(self, values=["Light", "Dark", "System"],
                                                      command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode) -> None:
        ctk.set_appearance_mode(new_appearance_mode)