#!/bin/python3

# pip install --user pyqrcode
# pip install --user pypng


import os
import pyqrcode
import png
from pyqrcode import QRCode
from time import sleep
os.system("clear")
#Função que gera QR Code de um link
def qr_link():

    # Clear
    os.system('clear')

    # Link desejado para o QRcode
    LINK = input('Cole aqui o link para gerar seu QRCode:\n\n')

    # Monta o QRCode
    code = pyqrcode.create(LINK)
    # Salva o QRCode gerado no local desejado
    PNG = input('\nDigite aqui o nome da sua imagem gerada (Exemplo: QRcode1.png):\n\n')
    code.png( f"{PNG}.png" , scale=8)

def qr_wifi():
        
    #Clear
    os.system("clear")

    # SSID desejado para o QRcode
    SSID = input('Cole aqui o SSID da rede para gerar seu QRCode:\n\n')
    #Clear
    os.system("clear")
    # tipo de seguranca
    SEC = int(input("""Digite o tipo de segurança da rede wi-fi\n
1) Nenhuma
2) WEP
3) WPA/WPA2-Personal\n\n"""))
    #Clear
    os.system("clear")
    if SEC == 1:
        code = pyqrcode.create(f"WIFI:S:{SSID};T:nopass;P:;;")
        # Salva o QRCode gerado no local desejado
        PNG = input('\nDigite aqui o nome da sua imagem gerada (Exemplo: QRcode1.png):\n\n')
        code.png( f"{PNG}.png" , scale=8)
    elif SEC == 2:
        # senha da rede
        PASS = input("Cole a senha do wi-fi que deseja incluir no QRcode\n\n")
        code = pyqrcode.create(f"WIFI:S:{SSID};T:WEP;P:{PASS};H:False;;")
        #Clear
        os.system("clear")
        PNG = input('\nDigite aqui o nome da sua imagem gerada (Exemplo: QRcode1.png):\n\n')
        code.png( f"{PNG}.png" , scale=8)
    elif SEC == 3:
        # senha da rede
        PASS = input("Cole a senha do wi-fi que deseja incluir no QRcode\n\n")
        #Clear
        os.system("clear")
        code = pyqrcode.create(f"WIFI:S:{SSID};T:WPA;P:{PASS};H:False;;")
        PNG = input('Digite aqui o nome da sua imagem gerada (Exemplo: QRcode1.png):\n\n')
        code.png( f"{PNG}.png" , scale=8)

def init():
    print("""Escolha o tipo de QRcode que você deseja criar:
1) Link
2) Senha de wi-fi\n""")
    opcao = int(input())

    if opcao == 1:
        qr_link()
    elif opcao == 2:
        qr_wifi()
    else:
        print("Opção não encontrada, tente novamente:")
        sleep(2)
        os.system("clear")
        init()

try:
    init()
except KeyboardInterrupt:
    os.system('clear')
    exit()