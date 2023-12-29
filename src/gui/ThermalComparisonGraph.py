from matplotlib import pyplot as plt

from src.image.RGBImage import RGBImage
from src.image.ThermalImage import ThermalImage


class ThermalComparisonGraph:
    # Obter as dimensões da imagem térmica
    # thermal_height, thermal_width = self.thermalImage.data.shape[:2]
    # Para o modelo C5 esperamos que se mantenha na forma: hermal_height, thermal_width = [120 , 160]
    # Calcular o deslocamento necessário para alinhar os recortes
    SCALING_FACTOR = 2.75
    CROP_RANGE = {  # Estes valores são obtidos de : cropped_rgb_image = rgb_np[y_offset:y_offset+int(2.75*thermal_height), x_offset:x_offset+int(2.75*thermal_width)]
        "xmin": 108,
        "xmax": 548,
        "ymin": 62,
        "ymax": 392
    }

    TEXT_OFFSET = {'x': 3.0, 'y': -5}
    THERMAL = 0
    RGB = 1


    def __init__(self, rgbImage: RGBImage, thermalImage: ThermalImage, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.rgbImage = rgbImage
        self.thermalImage = thermalImage

        self.fig, self.ax = plt.subplots(1, 2, figsize=(12, 6))

        self._cursorTextInit()
        self._temperatureTextInit()



    def _cursorTextInit(self):
        #Cursor a ser plotado na imagem termográfica
        self.cursor_text = {
            self.THERMAL : self.ax[self.THERMAL].annotate('', xy=(0, 0), xytext=(0, 0), textcoords='offset points', color='cyan'),
            self.RGB: self.ax[self.RGB].annotate('', xy=(0, 0), xytext=(0, 0), textcoords='offset points', color='cyan')
        }

        self.cursor_text[self.THERMAL].set_visible(False)
        self.cursor_text[self.RGB].set_visible(False)


    def _temperatureTextInit(self):
        #Texto do valor da temperatura para ser plotado na imagem termográfica
        self.temp_text = {
            self.THERMAL : self.ax[self.THERMAL].text(0, 0, "", color='white', bbox=dict(boxstyle="round,pad=0.3", fc='black', alpha=0.5)),
            self.RGB: self.ax[self.RGB].text(0, 0, "", color='white', bbox=dict(boxstyle="round,pad=0.3", fc='black', alpha=0.5))
        }
        self.temp_text[self.THERMAL].set_visible(False)
        self.temp_text[self.RGB].set_visible(False)
    def plot(self):
        # Recortar a imagem RGB para ficar igual à imagem térmica
        cropped_rgb_image = self.rgbImage.data[
                            self.CROP_RANGE["ymin"]:self.CROP_RANGE["ymax"],
                            self.CROP_RANGE["xmin"]:self.CROP_RANGE["xmax"]
                            ]

        # Plotar as imagens
        self.ax[0].imshow(self.thermalImage.data, cmap='hot')
        self.ax[1].imshow(cropped_rgb_image)

        # Títulos das imagens
        self.ax[0].set_title("Thermal Image")
        self.ax[1].set_title("RGB Image")

        # O mpl_connect faz com que a função seja ativada ao clicar com o mouse, relacionando o evento "clicar" com a função
        # self.fig.canvas.mpl_connect('button_release_event', self._on_button_release)
        self.fig.canvas.mpl_connect('motion_notify_event', self._update_temp_text)

        plt.show()


    def _update_temp_text(self, event):
        if event.inaxes == self.ax[1]:  # Quando o mouse estiver sobre a imagem RGB recortada
            x, y = round(event.xdata), round(event.ydata)
            x1, y1 = self._mapRGBToThermal(x, y)

            self._plotTemperatureText(x, y, x1, y1, self.RGB)
            self._plotCursorText(x1, y1, self.THERMAL)

            self.fig.canvas.draw_idle()

        elif event.inaxes == self.ax[0]:  # Quando o mouse estiver sobre a imagem térmica
            x, y = round(event.xdata), round(event.ydata)
            x1, y1 = self._mapThermalToRGB(x, y)

            self._plotTemperatureText(x, y, x, y, self.THERMAL)
            self._plotCursorText(x1, y1, self.RGB)

            self.fig.canvas.draw_idle()

        #------------------------------------
        # Desenvolvimento do zoom síncrono:
        # Funçao que copia o clique do mouse para a outra janela

    def _on_button_release(self, event):
        # Se o clique for na primeira imagem, faz uma cópia na segunda
        if event.inaxes == self.ax[0]:
            self._translateLimits(self.ax, 0, self.SCALING_FACTOR)
            self.fig.canvas.draw_idle()
        # Se o clique for na segunda imagem, faz uma cópia na primeira
        elif event.inaxes == self.ax[1]:
            self._translateLimits(self.ax, 1, 1 / self.SCALING_FACTOR)
            self.fig.canvas.draw_idle()

    @staticmethod
    def _translateLimits(axis, index: int, constant: float):
        limites_x = [(x*constant) for x in (axis[index].get_xlim())] # Consiste em obter os limites de x e y atuais da imagem Thermal, e para cada elemento da tupla (ax[0].get_xlim()) é multiplicado por 2,75, a qual se torna uma lista que diz qual deve ser os novos limites da imagem RGB recortada para coincidir com zoom feito na Thermal
        limites_y = [(y*constant) for y in (axis[index].get_ylim())] # Analogo ao anterior

        axis[not index].set_xlim(limites_x)   # Os limites da imagem RGB sao atualizados
        axis[not index].set_ylim(limites_y)

    def _plotCursorText(self, x, y, canvas: int):
        self.cursor_text[canvas].set_visible(True)
        self.cursor_text[not canvas].set_visible(False)
        self.cursor_text[canvas].set_text('+')
        self.cursor_text[canvas].set_fontsize(24)
        self.cursor_text[canvas].xy = (x, y)
        # self.cursor_text[canvas].xy = (x-5.5, y+3.0) # Correção da posição do cursor (a temperatura se mantém em x1,y1)

    def _plotTemperatureText(self, x, y, referenceX, referenceY, canvas: int):
        self.temp_text[canvas].set_visible(True)
        self.temp_text[not canvas].set_visible(False)
        temperature = self._getTemperatureFromPosition(referenceX, referenceY) # O valor da temperatura na posição x1,y1 (acurácia validada)

        #Caso seja desejado plotar a temperatura sobre a imagem RGB
        #temp_text_thermal_rgb.set_text(f'{temperature:.2f} ºC')
        #temp_text_thermal_rgb.set_position((x, y))

        self.temp_text[canvas].set_text(f'{temperature:.2f} ºC')
        self.temp_text[canvas].set_position((x + self.TEXT_OFFSET['x'], y + self.TEXT_OFFSET['x'])) #Correção da posição do texto, para não se sobrepor ao cursor

    def _getTemperatureFromPosition(self, x, y):
        return self.thermalImage.data[y, x]

    def _mapThermalToRGB(self, x, y):
        #Função para encontrar a correspondência entre as posições das imagens (aproximação calculada com dados visuais e refinamento dos mesmos)
        # A, B = 2.75034, 1.26921(valor calculado com dados visuais)
        # #Modifiquei o valor de B para zero, pois a expectativa é que a transformação seja linear (x1,y1)=(A*x,A*y)
        A, B = self.SCALING_FACTOR, 0.0
        x1 = round(A*x+B)
        y1 = round(A*y+B)

        return x1, y1

    def _mapRGBToThermal(self, x, y):
        A, B = self.SCALING_FACTOR, 0.0
        x1 = round((x-B)/A)
        y1 = round((y-B)/A)

        return x1, y1
