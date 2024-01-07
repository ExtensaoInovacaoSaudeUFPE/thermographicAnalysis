# import tkinter as tk
from tkinter import messagebox

# import ttkbootstrap as ttk
import customtkinter as ctk

from src.gui.ThermalComparisonGraph import ThermalComparisonGraph
from src.gui.routing.RoutedFrame import RoutedFrame
from src.image.ImageService import imageService
from src.image.types.RGBImage import RGBImage
from src.image.types.RawImage import RawImage
from src.image.types.ThermalImage import ThermalImage

MAX_IMAGE_SIZE = (400, 400)

class LoadedFrame(RoutedFrame):

    def __init__(self, master) -> None:
        super().__init__(master)

        self.mainText = ctk.CTkLabel(self,
                                     text="Imagem Mista",
                                     font=ctk.CTkFont(family="Helvetica", size=16, weight="bold"))
        self.mainText.pack(padx=8, pady=8)

        self.imageFrame = ctk.CTkFrame(self, width=400, height=400)
        self.imageFrame.pack(padx=8, pady=8, fill=ctk.BOTH, expand=True)

        self.imageLabel = ctk.CTkLabel(self.imageFrame, text="")
        self.imageLabel.pack(fill=ctk.BOTH, expand=True)

    def uiUpdate(self) -> None:
        try:
            self.setImage(imageService.getRawImage('main'))
        except Exception as e:
            messagebox.showerror("Erro", e.args[0])
            self.router.switchScreen("search")

    def setImage(self, image: RawImage) -> None:
        tkImage = image.toTkImage()
        self.imageLabel.configure(image=tkImage)
        self.imageLabel.image = tkImage
