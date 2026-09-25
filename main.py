import pywinauto
from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto.keyboard import send_keys
from pywinauto.mouse import click

import time 

caminho_chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
Website = "https://det.sit.trabalho.gov.br/login?r=%2Fservicos"

Application(backend="uia").start(caminho_chrome)
time.sleep(2)

area_trabalho = Desktop(backend="uia")
janela_chrome = area_trabalho.window(title_re=".*Google Chrome", found_index=0)
janela_chrome.wait('ready', timeout=10)

send_keys('^l')
send_keys(Website)
send_keys('{ENTER}')

botao_entrar = janela_chrome.child_window(title="Entrar com  gov.br", control_type="Button")
botao_entrar.invoke()

time.sleep(2)

botao_certificado = janela_chrome.child_window(title_re=".*certificado digital.*", control_type="Button", found_index= 0)
botao_certificado.wait('visible', timeout=15)
botao_certificado.invoke()