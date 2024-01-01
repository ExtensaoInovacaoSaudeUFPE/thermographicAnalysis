from matplotlib import pyplot as plt

from src.image.RGBImage import RGBImage
from src.image.ThermalImage import ThermalImage


class ThermalComparisonGraph:
    # Obter as dimensões da imagem térmica
    # thermal_height, thermal_width = self.thermalImage.data.shape[:2]
    # Para o modelo C5 esperamos que se mantenha na forma: hermal_height, thermal_width = [120 , 160]
    SCALING_FACTOR = 2.75
    CROP_RANGE = {  # Estes valores são obtidos de : cropped_rgb_image = rgb_np[y_offset:y_offset+int(2.75*thermal_height), x_offset:x_offset+int(2.75*thermal_width)]
        "xmin": 108,
        "xmax": 548,
        "ymin": 62,
        "ymax": 392
    }

    TEXT_OFFSET = {'x': 3.0, 'y': -5}
    CURSOR_OFFSET = {'x': 0, 'y': 0}  #{'x': -5.5, 'y': 3}  # Correção visual da posição do cursor

    THERMAL, RGB = 0, 1

    def __init__(self, rgbImage: RGBImage, thermalImage: ThermalImage):
        self.rgbImage = rgbImage
        self.thermalImage = thermalImage
        self.croppedRGBImage = self.rgbImage.crop(self.CROP_RANGE["xmin"], self.CROP_RANGE["xmax"], self.CROP_RANGE["ymin"], self.CROP_RANGE["ymax"])

        self._canvasInit()
        self._cursorTextInit()
        self._temperatureTextInit()
        self._linkEvents()


    def plot(self):
        self.ax[0].imshow(self.thermalImage.data, cmap='hot')
        self.ax[1].imshow(self.croppedRGBImage.data)

        plt.show()

    def _canvasInit(self):
        self.fig, self.ax = plt.subplots(1, 2, figsize=(12, 6))

        self.ax[0].set_title("Imagem Termográfica")
        self.ax[1].set_title("Imagem RGB")

    def _cursorTextInit(self):
        self.cursor_text = {
            self.THERMAL : self.ax[self.THERMAL].annotate('', xy=(0, 0), xytext=(0, 0), textcoords='offset points', color='cyan'),
            self.RGB: self.ax[self.RGB].annotate('', xy=(0, 0), xytext=(0, 0), textcoords='offset points', color='cyan')
        }

        self.cursor_text[self.THERMAL].set_visible(False)
        self.cursor_text[self.RGB].set_visible(False)

    def _temperatureTextInit(self):
        self.temp_text = {
            self.THERMAL : self.ax[self.THERMAL].text(0, 0, "", color='white', bbox=dict(boxstyle="round,pad=0.3", fc='black', alpha=0.5)),
            self.RGB: self.ax[self.RGB].text(0, 0, "", color='white', bbox=dict(boxstyle="round,pad=0.3", fc='black', alpha=0.5))
        }
        self.temp_text[self.THERMAL].set_visible(False)
        self.temp_text[self.RGB].set_visible(False)

    def _linkEvents(self):
        # O mpl_connect faz com que a função seja ativada ao clicar com o mouse, relacionando o evento "clicar" com a função
        self.fig.canvas.mpl_connect('button_release_event', self._onButtonRelease)
        self.fig.canvas.mpl_connect('motion_notify_event', self._updateTemperatureTextAndCursor)

    def _onButtonRelease(self, event):
        # Desenvolvimento do zoom síncrono:
        # Funçao que copia o clique do mouse para a outra janela
        if event.inaxes == self.ax[0]:  # Se o clique for na primeira imagem, faz uma cópia na segunda
            self._translateImageLimits(0, self.SCALING_FACTOR)
            self.fig.canvas.draw_idle()

        elif event.inaxes == self.ax[1]:  # Se o clique for na segunda imagem, faz uma cópia na primeira
            self._translateImageLimits(1, 1 / self.SCALING_FACTOR)
            self.fig.canvas.draw_idle()

    def _translateImageLimits(self, canvas: int, gain: float):
        limites_x = [(x * gain) for x in (self.ax[canvas].get_xlim())] # Consiste em obter os limites de x e y atuais da imagem RGB ou Termica, e para cada elemento da tupla (ax[0].get_xlim()) é multiplicado por 2,75, a qual se torna uma lista que diz qual deve ser os novos limites da imagem RGB recortada para coincidir com zoom feito na Thermal
        limites_y = [(y * gain) for y in (self.ax[canvas].get_ylim())] # Analogo ao anterior

        self.ax[int(not canvas)].set_xlim(limites_x)   # Os limites da outra imagem sao atualizados
        self.ax[int(not canvas)].set_ylim(limites_y)

    def _updateTemperatureTextAndCursor(self, event):
        if (event.inaxes == self.ax[0] or self.ax[1]) and event.xdata is not None and event.ydata is not None:
            x, y = round(event.xdata), round(event.ydata)

            if event.inaxes == self.ax[1]:  # Quando o mouse estiver sobre a imagem RGB recortada
                x1, y1 = self._mapRGBToThermal(x, y)
                self._plotCursorText(x1, y1, self.THERMAL)
                self._plotTemperatureText(x, y, x1, y1, self.RGB)

            else:  # Quando o mouse estiver sobre a imagem térmica
                x1, y1 = self._mapThermalToRGB(x, y)
                self._plotCursorText(x1, y1, self.RGB)
                self._plotTemperatureText(x, y, x, y, self.THERMAL)

            self.fig.canvas.draw_idle()

    def _plotCursorText(self, x, y, canvas: int):
        self.cursor_text[canvas].set_visible(True)
        self.cursor_text[int(not canvas)].set_visible(False)

        self.cursor_text[canvas].set_text('+')
        self.cursor_text[canvas].set_fontsize(24)
        self.cursor_text[canvas].xy = (x + self.CURSOR_OFFSET['x'], y + self.CURSOR_OFFSET['y'])

    def _plotTemperatureText(self, x, y, referenceX, referenceY, canvas: int):
        self.temp_text[canvas].set_visible(True)
        self.temp_text[int(not canvas)].set_visible(False)

        temperature = self.thermalImage.getTemperatureAt(referenceX, referenceY)
        self.temp_text[canvas].set_text(f'{temperature:.2f} ºC')
        self.temp_text[canvas].set_position((x + self.TEXT_OFFSET['x'], y + self.TEXT_OFFSET['x']))

    def _mapThermalToRGB(self, x: float, y: float) -> (int, int):
        #Função para encontrar a correspondência entre as posições das imagens (aproximação calculada com dados visuais e refinamento dos mesmos)
        # A, B = 2.75034, 1.26921(valor calculado com dados visuais) # #Modifiquei o valor de B para zero, pois a expectativa é que a transformação seja linear (x1,y1)=(A*x,A*y)
        A, B = self.SCALING_FACTOR, 0.0
        x1 = round(A*x+B)
        y1 = round(A*y+B)

        return x1, y1

    def _mapRGBToThermal(self, x: float, y: float) -> (int, int):
        A, B = self.SCALING_FACTOR, 0.0
        x1 = round((x-B)/A)
        y1 = round((y-B)/A)

        return x1, y1
