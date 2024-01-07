import tkinter as tk
from tkinter import filedialog, messagebox

import ttkbootstrap as ttk

from src.gui.routing.RoutedFrame import RoutedFrame
from src.image.ImageService import imageService


class SearchFrame(RoutedFrame):
    def __init__(self, master: tk.Misc) -> None:
        super().__init__(master)

        self.mainText = ttk.Label(self, text="Análise Termográfica", font="Helvetica 16 bold")
        self.mainText.pack(pady=10, padx=10)
        self.searchImageButton = ttk.Button(self, text="Importar Imagem", command=self.searchImagePath)
        self.searchImageButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def searchImagePath(self) -> None:
        path = filedialog.askopenfilename()
        try:
            imageService.importImage(path, 'main')
        except Exception as e:
            messagebox.showerror("Erro", e.args[0])
            return
        self.router.switchScreen("loaded")

