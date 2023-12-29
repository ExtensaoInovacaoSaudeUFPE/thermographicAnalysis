import tkinter as tk
from tkinter import filedialog
from flir_image_extractor_C5_cZS import FlirImageExtractor
import argparse
from PIL import Image, ImageTk

def processar_imagem(file_path):
    parser = argparse.ArgumentParser(description='Exemplo de processamento de imagem com FlirImageExtractor')
    parser.add_argument('-d', '--debug', help='Ativar o modo de depuração', required=False, action='store_true')
    args = parser.parse_args()

    fie = FlirImageExtractor(exiftool_path=r'C:/Users/gabri/OneDrive/Área de Trabalho/alt2/Programação/Python/Projextensão zoom imagem/FlirImageExtractor-master/exiftool.exe', is_debug=args.debug)

    fie.process_image(file_path)
    rgb_image = fie.get_rgb_np()
    
    original_image = Image.open(file_path)
    original_image = ImageTk.PhotoImage(original_image)

    original_window = tk.Toplevel()
    original_window.title("Imagem Original")
    
    label_original = tk.Label(original_window, image=original_image)
    label_original.pack()
    
    fie.plot()
    
def abrir_arquivo():
    file_path = filedialog.askopenfilename()
    if file_path:
        print("Arquivo selecionado:", file_path)
        processar_imagem(file_path)

def fechar_programa():
    root.quit()

root = tk.Tk()
root.title("Menu projextensao")
root.geometry("300x250")

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Arquivo", menu=file_menu)
file_menu.add_command(label="Abrir Arquivo", command=abrir_arquivo)

root.mainloop()
