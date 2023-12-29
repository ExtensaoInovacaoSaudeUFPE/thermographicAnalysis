# import ttkbootstrap as ttk
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from src.gui.ThermalComparisonGraph import ThermalComparisonGraph
from src.infra.FlirImageFactory import FlirImageFactory


class Home(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Menu projextensao")
        self.geometry("300x250")

        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Arquivo", menu=file_menu)
        file_menu.add_command(label="Abrir Arquivo", command=self.abrir_arquivo)
        file_menu.add_command(label="Fechar", command=self.fechar_programa)

    def processar_imagem(self, file_path: str):
        rgb_image = FlirImageFactory.getRGBImageFromPath(file_path)
        thermal_image = FlirImageFactory.getThermalImageFromPath(file_path)

        original_image = Image.open(file_path)
        original_image = ImageTk.PhotoImage(original_image)

        original_window = tk.Toplevel()
        original_window.title("Imagem Original")

        label_original = tk.Label(original_window, image=original_image)
        label_original.pack()

        ThermalComparisonGraph(rgb_image, thermal_image).plot()

    def abrir_arquivo(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            print("Arquivo selecionado:", file_path)
            self.processar_imagem(file_path)

    def fechar_programa(self):
        self.quit()
