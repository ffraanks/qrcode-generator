#!/bin/python3

# pip install --user pyqrcode
# pip install --user pypng

import os
import pyqrcode
import png
from pyqrcode import QRCode

# Clear
os.system('clear')

# Link desejado para o QRcode
LINK = input('Cole aqui o link para gerar seu QRCode:\n\n')

# Monta o QRCode
url = pyqrcode.create(LINK)

# Salva o QRCode gerado no local desejado
PNG = input('\nDigite aqui o nome da sua imagem gerada (Exemplo: QRcode1.png):\n\n')
url.png( PNG , scale=8)
