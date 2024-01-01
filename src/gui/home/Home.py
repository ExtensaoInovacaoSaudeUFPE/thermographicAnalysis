import ttkbootstrap as ttk
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from threading import Thread
from src.gui.ThermalComparisonGraph import ThermalComparisonGraph
from src.infra.FlirImageFactory import FlirImageFactory



class Home(tk.Tk):
    _windowTitle = "Análise Termográfica"
    _startGeometry = "500x500"


    currentFilePath = ""
    _imageSelected = False

    def __init__(self):
        super().__init__()

        self.title(self._windowTitle)
        self.geometry(self._startGeometry)
        self._setupMenu()
        self._createWidgets()
        self._setupLayout()


    def _setupMenu(self):
        self.menu_bar = ttk.Menu(self)
        file_menu = ttk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_command(label="Ajuda", command=self._helpMessage)

        self.config(menu=self.menu_bar)

    def _createWidgets(self):
        self.mainText = ttk.Label(self, text="Análise Termográfica", font="Helvetica 16 bold")
        self.imageFrame = ttk.Labelframe(self, width=400, height=400, text="Imagem Original", padding="20 20 20 20")
        self.searchImageButton = ttk.Button(self, text="Importar Imagem", command=self._searchFile)
        self.optionsFrame = ttk.Frame(self)
        self.viewThermalPlotButton = ttk.Button(self.optionsFrame, text="Ver Gráfico", command=self._openThermalComparisonGraph)
        self.searchAnotherImageButton = ttk.Button(self.optionsFrame, text="Importar Outra Imagem", command=self._searchFile)
        self.imageLabel = None

    def _updateWidgets(self):
        if self._imageSelected:
            self._viewLayout()
        else:
            self._searchLayout()


    def _searchLayout(self):
        self.imageFrame.pack_forget()
        self.viewThermalPlotButton.pack_forget()
        self.searchAnotherImageButton.pack_forget()
        self.searchImageButton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def _viewLayout(self):
        self.imageFrame.pack(padx=10, pady=10)
        self.optionsFrame.pack(padx=10, pady=10)
        self.viewThermalPlotButton.pack(pady=10, side=tk.LEFT)
        self.searchAnotherImageButton.pack(pady=10, side=tk.LEFT)

        if self.imageLabel:
            self.imageLabel.pack()
        self.searchImageButton.place_forget()

    def _setupLayout(self):
        self.mainText.pack(pady=10)
        self._updateWidgets()


    def _processImage(self):
        if not self.currentFilePath:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado")
            return

        possible_image = Image.open(self.currentFilePath)

        if not possible_image:
            messagebox.showerror("Erro", "Imagem inválida")
            return

        self.original_image = possible_image

        if self.imageLabel:
            self.imageLabel.pack_forget()

        max_size = (400, 400)
        self.original_image.thumbnail(max_size)
        self.original_image = ImageTk.PhotoImage(self.original_image)
        self.imageLabel = tk.Label(self.imageFrame, image=self.original_image)
        self._imageSelected = True
        self._updateWidgets()

    def _openThermalComparisonGraph(self):
        if not self.currentFilePath:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado")
            return
        rgb_image = FlirImageFactory.getRGBImageFromPath(self.currentFilePath)
        thermal_image = FlirImageFactory.getThermalImageFromPath(self.currentFilePath)

        ThermalComparisonGraph(rgb_image, thermal_image).plot()

    def _searchFile(self):
        path = filedialog.askopenfilename()
        if not path:
            messagebox.showerror("Erro", "Nenhum arquivo selecionado")
            return

        self.currentFilePath = path
        self._processImage()

    def _helpMessage(self):
        messagebox.showinfo("Ajuda", "Para utilizar o programa, basta selecionar uma imagem termográfica após clicar no botão 'Procurar Imagem' e clicar no botão 'Ver Plot' para visualizar o gráfico de comparação termográfica. Poderá ser feito zoom nas imagens a partir da lupa.")
