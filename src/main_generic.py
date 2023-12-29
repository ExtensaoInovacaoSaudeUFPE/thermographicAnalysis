# import flir_image_extractor
from dependencies.flir_image_extractor import FlirImageExtractor

# Especificando o caminho do exitfool
caminho_exiftool = r'AQUI ESTARÁ O CAMINHO DO EXIFTOOL' 

# Criando o objeto de extracao
fir = FlirImageExtractor(exiftool_path=caminho_exiftool)

# Especificando o caminho da imagem
caminho_imagem = r'AQUI ESTARÁ O CAMINHO DA IMAGEM QUE SERÁ PROCESSADA'

fir.process_image(caminho_imagem)
fir.plot()