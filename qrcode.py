#!/bin/python3

# pip install --user pyqrcode
# pip install --user pypng

import os
import pyqrcode
import png
from pyqrcode import QRCode
from time import sleep

if os.name == 'posix':
    cls = "clear"
else:
    cls = "cls"

os.system(cls)

#Função que gera QR Code de um link
def qr_link():

    # Clear
    os.system(cls)

    # Link desejado para o QRcode
    LINK = input('Cole aqui o link para gerar seu QRCode:\n\n')

    # Monta o QRCode
    code = pyqrcode.create(LINK)
    # Salva o QRCode gerado no local desejado
    PNG = input('\nDigite aqui o nome da sua imagem gerada (Exemplo: QRcode1.png):\n\n')
    code.png( f"{PNG}.png" , scale=8)

def qr_wifi():

    #Clear
    os.system(cls)

    # SSID desejado para o QRcode
    SSID = input('Cole aqui o SSID da rede para gerar seu QRCode:\n\n')
    #Clear
    os.system(cls)
    # tipo de seguranca
    SEC = int(input("""Digite o tipo de segurança da rede wi-fi\n
1) Nenhuma
2) WEP
3) WPA/WPA2-Personal\n\n"""))
    #Clear
    os.system(cls)
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
        os.system(cls)
        PNG = input('\nDigite aqui o nome da sua imagem gerada (Exemplo: QRcode1.png):\n\n')
        code.png( f"{PNG}.png" , scale=8)
    elif SEC == 3:
        # senha da rede
        PASS = input("Cole a senha do wi-fi que deseja incluir no QRcode\n\n")
        #Clear
        os.system(cls)
        code = pyqrcode.create(f"WIFI:S:{SSID};T:WPA;P:{PASS};H:False;;")
        PNG = input('Digite aqui o nome da sua imagem gerada (Exemplo: QRcode1.png):\n\n')
        code.png( f"{PNG}.png" , scale=8)


def qr_email():
    os.system(cls)

    DEST = input("Digite o destinatário do e-mail:\n\n")

    os.system(cls)

    ASSUNTO = input("Digite o assunto do e-mail:\n\n")

    os.system(cls)

    CONTEUDO = input("Digite aqui o conteudo do email:\n\n")

    os.system(cls)

    code = pyqrcode.create(f"MATMSG:TO:{DEST};SUB:{ASSUNTO};BODY:{CONTEUDO};;")
    PNG = input('Digite aqui o nome da sua imagem gerada (Exemplo: QRcode1.png):\n\n')
    code.png( f"{PNG}.png" , scale=8)

def basic_contact():
    os.system(cls)

    P_NOME = str(input("Digite o primeiro nome do contato:\n\n"))

    os.system(cls)

    S_NOME = str(input("Digite o sobrenome do contato:\n\n"))
    
    os.system(cls)

    TEL = input("Digite o número de telefone do contato:\n\n")

    os.system(cls)

    code = pyqrcode.create(f"""BEGIN:VCARD
VERSION:2.1
N;CHARSET=UTF-8:{S_NOME};{P_NOME}
FN;CHARSET=UTF-8:{P_NOME} {S_NOME}
TEL:{TEL}
END:VCARD""")

    PNG = input('Digite aqui o nome da sua imagem gerada (Exemplo: QRcode1.png):\n\n')
    code.png( f"{PNG}.png" , scale=8)

def contact():
    os.system(cls)

    P_NOME = str(input("Digite o primeiro nome do contato:\n\n"))

    os.system(cls)

    S_NOME = str(input("Digite o sobrenome do contato:\n\n"))
    
    os.system(cls)

    TEL = input("Digite o número de telefone do contato:\n\n")

    os.system(cls)

    COMP = input("Digite o nome da empresa ou companhia do contato:\n\n")

    os.system(cls)

    CARGO = input('Digite seu cargo dentro da empresa:\n\n')

    os.system(cls)

    EMAIL = input("Digite o E-mail do contato:\n\n")

    os.system(cls)

    code = pyqrcode.create(f"""BEGIN:VCARD
VERSION:2.1
N;CHARSET=UTF-8:{S_NOME};{P_NOME}
FN;CHARSET=UTF-8:{P_NOME} {S_NOME}
ORG:{COMP}
TITLE:{CARGO}
TEL:{TEL}
EMAIL:{EMAIL}
END:VCARD""")

    PNG = input('Digite aqui o nome da sua imagem gerada (Exemplo: QRcode1.png):\n\n')
    code.png( f"{PNG}.png" , scale=8)


def init():
    print("""Escolha o tipo de QRcode que você deseja criar:
1) Link
2) Senha de wi-fi
3) E-Mail
4) Contato Básico
5) Contato
""")
    opcao = int(input())

    if opcao == 1:
        qr_link()
    elif opcao == 2:
        qr_wifi()
    elif opcao == 3:
        qr_email()
    elif opcao == 4:
        basic_contact()
    elif opcao == 5:
        contact()
    else:
        print("Opção não encontrada, tente novamente:")
        sleep(2)
        os.system(cls)
        init()

try:
    init()
except KeyboardInterrupt:
    os.system(cls)
    exit()
