import tkinter as tk
from tkinter import messagebox

import ttkbootstrap as ttk

from src.gui.ThermalComparisonGraph import ThermalComparisonGraph
from src.gui.routing.RoutedFrame import RoutedFrame
from src.image.ImageService import imageService
from src.image.types.RGBImage import RGBImage
from src.image.types.RawImage import RawImage
from src.image.types.ThermalImage import ThermalImage

MAX_IMAGE_SIZE = (400, 400)

class LoadedFrame(RoutedFrame):

    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)

        self.mainText = ttk.Label(self, text="Análise Termográfica", font="Helvetica 16 bold")
        self.mainText.pack(pady=8)

        self.imageFrame = ttk.Labelframe(self, width=400, height=400, text="Imagem Original", padding="16 16 16 16")
        self.imageFrame.pack(padx=16, pady=8)

        self.optionsFrame = ttk.Frame(self)
        self.optionsFrame.pack(pady=8)

        self.viewThermalPlotButton = ttk.Button(self.optionsFrame,
                                                text="Ver Gráfico",
                                                command= lambda: self.router.switchScreen("comparison"))
        self.viewThermalPlotButton.pack(side=tk.LEFT)

        self.searchAnotherImageButton = ttk.Button(self.optionsFrame,
                                                   text="Importar Outra Imagem",
                                                   command=lambda: self.router.switchScreen("search"))
        self.searchAnotherImageButton.pack(side=tk.LEFT)

        self.imageLabel = tk.Label(self.imageFrame)
        self.imageLabel.pack(fill=tk.BOTH, expand=True)

    def uiUpdate(self) -> None:
        try:
            self.setImage(imageService.getRawImage('main'))
        except Exception as e:
            messagebox.showerror("Erro", e.args[0])
            self.router.switchScreen("search")

    def setImage(self, image: RawImage) -> None:
        tkImage = image.toTkImage(MAX_IMAGE_SIZE)
        self.imageLabel.configure(image=tkImage)
        self.imageLabel.image = tkImage
