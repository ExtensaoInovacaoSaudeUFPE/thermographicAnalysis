import tkinter as tk
from typing import Callable

import ttkbootstrap as ttk

from src.image.Image import Image

MAX_IMAGE_SIZE = (400, 400)

class LoadedFrame(tk.Frame):

    def __init__(self, window: tk.Tk) -> None:
        super().__init__(window)

        self.mainText = ttk.Label(self, text="Análise Termográfica", font="Helvetica 16 bold")
        self.mainText.pack(pady=8)

        self.imageFrame = ttk.Labelframe(self, width=400, height=400, text="Imagem Original", padding="16 16 16 16")
        self.imageFrame.pack(padx=16, pady=8)

        self.optionsFrame = ttk.Frame(self)
        self.optionsFrame.pack(pady=8)

        self.viewThermalPlotButton = ttk.Button(self.optionsFrame, text="Ver Gráfico")
        self.viewThermalPlotButton.pack(side=tk.LEFT)

        self.searchAnotherImageButton = ttk.Button(self.optionsFrame, text="Importar Outra Imagem")
        self.searchAnotherImageButton.pack(side=tk.LEFT)

        self.imageLabel = tk.Label(self.imageFrame)
        self.imageLabel.pack(fill=tk.BOTH, expand=True)

    def bindThermalPlotButton(self, callback: Callable[[], None]) -> None:
        self.viewThermalPlotButton.configure(command=callback)

    def bindSearchAnotherImageButton(self, callback: Callable[[], None]) -> None:
        self.searchAnotherImageButton.configure(command=callback)

    def setImage(self, image: Image) -> None:
        tkImage = image.toTkImage(MAX_IMAGE_SIZE)
        self.imageLabel.configure(image=tkImage)
        self.imageLabel.image = tkImage
