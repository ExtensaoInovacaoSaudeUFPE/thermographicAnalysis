import tkinter as tk
from tkinter import filedialog, messagebox

# import ttkbootstrap as ttk
import customtkinter as ctk
from src.gui.routing.RoutedFrame import RoutedFrame
from src.image.ImageService import imageService


class SearchFrame(RoutedFrame):
    def __init__(self, master) -> None:
        super().__init__(master)

        self.mainText = ctk.CTkLabel(self,
                                     text="Análise Termográfica",
                                     font=ctk.CTkFont(family="Helvetica", size=16, weight="bold"))
        self.mainText.pack(pady=8, padx=8)
        self.searchImageButton = ctk.CTkButton(self, text="Importar Imagem", command=self.searchImagePath)
        self.searchImageButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def searchImagePath(self) -> None:
        path = filedialog.askopenfilename()
        try:
            imageService.importImage(path, 'main')
        except Exception as e:
            messagebox.showerror("Erro", e.args[0])
            return
        self.router.switchScreen("loaded")

