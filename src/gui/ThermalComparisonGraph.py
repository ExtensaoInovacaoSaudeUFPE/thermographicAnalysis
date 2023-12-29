from matplotlib import pyplot as plt

from src.image.RGBImage import RGBImage
from src.image.ThermalImage import ThermalImage


class ThermalComparisonGraph:
    def __init__(self, rgbImage: RGBImage, thermalImage: ThermalImage, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.rgbImage = rgbImage
        self.thermalImage = thermalImage

    def plot(self, *args, **kwargs):

        # Obter as dimensões da imagem térmica
        thermal_height, thermal_width = self.thermalImage.data.shape[:2]
        # Para o modelo C5 esperamos que se mantenha na forma: hermal_height, thermal_width = [120 , 160]

        # Calcular o deslocamento necessário para alinhar os recortes
        y_offset = 62 #Ajuste visual refinado
        x_offset = 108 #Ajuste visual refinado

        # Recortar a imagem RGB para ficar igual à imagem térmica
        cropped_rgb_image = self.rgbImage.data[y_offset:392, x_offset:548]
        # Estes valores acima são obtidos de : cropped_rgb_image = rgb_np[y_offset:y_offset+int(2.75*thermal_height), x_offset:x_offset+int(2.75*thermal_width)]

        fig, ax = plt.subplots(1,2, figsize=(12, 6))

        # Plotar as imagens
        ax[0].imshow(self.thermalImage.data, cmap='hot')
        ax[1].imshow(cropped_rgb_image)

        # Títulos das imagens
        ax[0].set_title("Thermal Image")
        ax[1].set_title("RGB Image")

        #Cursor a ser plotado na imagem termográfica
        cursor_text_thermal = ax[0].annotate('', xy=(0, 0), xytext=(0, 0), textcoords='offset points', color='cyan')
        cursor_text_thermal.set_visible(False)

        #Cursor a ser plotado na imagem RGB
        cursor_text_rgb = ax[1].annotate('', xy=(0, 0), xytext=(0, 0), textcoords='offset points', color='cyan')
        cursor_text_rgb.set_visible(False)

        #Texto do valor da temperatura para ser plotado na imagem termográfica
        temp_text_thermal = ax[0].text(0, 0, "", color='white', bbox=dict(boxstyle="round,pad=0.3",fc='black', alpha=0.5))

        #Texto do valor da temperatura para ser plotado na imagem rgb recortada
        temp_text_thermal_rgb = ax[1].text(0, 0, "", color='white', bbox=dict(boxstyle="round,pad=0.3",fc='black', alpha=0.5))

        def update_temp_text(event):
            if not event.inaxes or event.inaxes == ax[1]: #Quando o mouse estiver sobre a imagem RGB recortada
                x, y = round(event.xdata), round(event.ydata)

                #Função para encontrar a correspondência entre as posições das imagens (aproximação calculada com dados visuais e refinamento dos mesmos)
                A = 2.75 #2.75034 (valor calculado com dados visuais)
                B = 0.0 #1.26921 (valor calculado com dados visuais)
                #Modifiquei o valor de B para zero, pois a expectativa é que a transformação seja linear (x1,y1)=(A*x,A*y)
                x1 = round((x-B)/A)
                y1 = round((y-B)/A)

                temperature = self.thermalImage.data[y1,x1] # O valor da temperatura na posição x1,y1 (acurácia validada)

                #Caso seja desejado plotar a temperatura sobre a imagem RGB
                #temp_text_thermal_rgb.set_text(f'{temperature:.2f} ºC')
                #temp_text_thermal_rgb.set_position((x, y))

                temp_text_thermal.set_text(f'{temperature:.2f} ºC')
                temp_text_thermal.set_position((x1+3.0, y1-5.0)) #Correção da posição do texto, para não se sobrepor ao cursor

                cursor_text_thermal.set_visible(True)
                #cursor_text_thermal.xy = (x1-5.5, y1+3.0) # Correção da posição do cursor (a temperatura se mantém em x1,y1)
                cursor_text_thermal.xy = (x1, y1)
                cursor_text_thermal.set_text('+')
                cursor_text_thermal.set_fontsize(24)

                #Deixando o cursor sobre a imagem RGB invisível
                cursor_text_rgb.set_visible(False)

                fig.canvas.draw_idle()
                return

            x, y = round(event.xdata), round(event.ydata)
            #if 0<= x < thermal_np.shape[1] and 0<= y < thermal_np.shape[0]
            if not event.inaxes or event.inaxes == ax[0]: #Quando o mouse estiver sobre a imagem térmica
                #Modifique caso queira plotar a temperatura sobre a imagem RGB simultaneamente
                temp_text_thermal_rgb.set_text("")

                #Valor extato na temperatura
                temperature = self.thermalImage.data[y,x]
                temp_text_thermal.set_text(f'{temperature:.2f} ºC')
                temp_text_thermal.set_position((x+4, y-4)) #offset para não ficar em cima do mouse

                #Cursor sobre a imagem termética não será exibido
                cursor_text_thermal.set_visible(False)

                #Correspondência inversa da x1,y1
                A = 2.75 #2.75034 (valor calculado com dados visuais)
                B = 0.0 #1.26921 (valor calculado com dados visuais)
                #Modifiquei o valor de B para zero, pois a expectativa é que a transformação seja linear (x2,y2)=(A*x,A*y)
                x2 = round(A*x+B)
                y2 = round(A*y+B)

                #Exibindo um cursor sobre a imagem RGB
                cursor_text_rgb.set_visible(True)
                #cursor_text_rgb.xy = (x2-9.0, y2+12.0) # Ajuste da posição do cursor na imagem RGB
                cursor_text_rgb.xy = (x2, y2)
                cursor_text_rgb.set_text('+')
                cursor_text_rgb.set_fontsize(24)

                fig.canvas.draw_idle()

        #------------------------------------
        # Desenvolvimento do zoom síncrono:
        # Funçao que copia o clique do mouse para a outra janela
        def on_button_release(event):
            # Se o clique for na primeira imagem, faz uma cópia na segunda
            if event.inaxes == ax[0]:
                limites_x = [(x*2.75) for x in (ax[0].get_xlim())] # Consiste em obter os limites de x e y atuais da imagem Thermal, e para cada elemento da tupla (ax[0].get_xlim()) é multiplicado por 2,75, a qual se torna uma lista que diz qual deve ser os novos limites da imagem RGB recortada para coincidir com zoom feito na Thermal
                limites_y = [(y*2.75) for y in (ax[0].get_ylim())] # Analogo ao anterior

                ax[1].set_xlim(limites_x)   # Os limites da imagem RGB sao atualizados
                ax[1].set_ylim(limites_y)

                fig.canvas.draw_idle()
            # Se o clique for na segunda imagem, faz uma cópia na primeira
            elif event.inaxes == ax[1]:
                limites_x = [(x/2.75) for x in (ax[1].get_xlim())]   # Consiste em obter os limites de x e y atuais da imagem RGB, e para cada elemento da tupla (ax[0].get_xlim()) é dividido por 2,75, a qual se torna uma lista que diz qual deve ser os novos limites da imagem Thermal para coincidir com zoom feito na RGB
                limites_y = [(y/2.75) for y in (ax[1].get_ylim())]

                ax[0].set_xlim(limites_x)   # Os limites da imagem Thermal sao atualizados
                ax[0].set_ylim(limites_y)

                fig.canvas.draw_idle()

        # O mpl_connect faz com que a função seja ativada ao clicar com o mouse, relacionando o evento "clicar" com a função
        fig.canvas.mpl_connect('button_release_event', on_button_release)
        #------------------------------------

        fig.canvas.mpl_connect('motion_notify_event', update_temp_text)

        plt.show()
