import tkinter as tk
from typing import Callable

import ttkbootstrap as ttk

class SearchFrame(tk.Frame):
    def __init__(self, window: tk.Tk):
        super().__init__(window)

        self.mainText = ttk.Label(self, text="Análise Termográfica", font="Helvetica 16 bold")
        self.mainText.pack(pady=10)

        self.searchImageButton = ttk.Button(self, text="Importar Imagem")
        self.searchImageButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


    def bindSearchImageButton(self, callback: Callable[[], None]) -> None:
        self.searchImageButton.configure(command=callback)