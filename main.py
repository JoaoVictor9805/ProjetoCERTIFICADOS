import config_logger
import pywinauto
from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto.keyboard import send_keys
from pywinauto.mouse import click
from pywinauto.timings import TimeoutError as PywinautoTimeoutError
from pywinauto.findwindows import ElementNotFoundError, ElementAmbiguousError

from config_logger import iniciar_logger
import logging
import time 

caminho_chrome  = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
website         = "https://det.sit.trabalho.gov.br/login?r=%2Fservicos"
caminho_web     = f'"{caminho_chrome}" {website}'

# =================
# 1. Iniciar log e notificar início da automação
# =================

iniciar_logger()
logging.info("--- Iniciando automação do portal gov.br ---")

# =================
# 2. Abertura do navegador
# =================

try:
    logging.info("Tentando abrir o Google Chrome...")

    Application(backend="uia").start(caminho_web)
    time.sleep(2)

    logging.info("Comando de abertura enviado com sucesso.")

except Exception as e:
    logging.exception(f"Falha crítica ao tentar abrir o Chrome: {e}")
    exit()


# =================
# 2. Mapeamento do Desktop e Foco na Janela
# =================

try:
    logging.info("Procurando a janela do Chrome na área de trabalho...")

    area_trabalho = Desktop(backend="uia")
    janela_chrome = area_trabalho.window(title_re=".*Google Chrome", found_index=0)
    janela_chrome.wait('ready', timeout=10)

    logging.info("Janela do Chrome encontrada e pronta para uso.")

except PywinautoTimeoutError:
    logging.error("O tempo esgotou (10s) e a janela do Chrome não ficou pronta.")
    exit()

except ElementNotFoundError:
    logging.error("Nenhuma janela com o título 'Google Chrome' foi encontrada na tela.")
    exit()


# =================
# 4. Interação com Botões
# =================

try:
    logging.info("Buscando o botão 'Entrar com gov.br'...")

    botao_entrar = janela_chrome.child_window(
        title="Entrar com  gov.br", 
        control_type="Button"
    )
    botao_entrar.wait('visible', timeout=15)
    botao_entrar.invoke()

    logging.info("Clique no botão 'Entrar com gov.br' realizado.")

    time.sleep(2)

    logging.info("Buscando o botão 'Certificado digital'...")

    botao_certificado = janela_chrome.child_window(
        title_re=".*certificado digital.*", 
        control_type="Button", 
        found_index= 0
    )
    botao_certificado.wait('visible', timeout=15)
    botao_certificado.invoke()
    logging.info("Clique no botão 'Certificado digital' realizado com sucesso.")

except ElementNotFoundError as e:
    logging.error("Um dos botões não foi encontrado na tela. A página pode não ter carregado corretamente.")
    logging.debug(f"Detalhes técnicos: {e}")
except ElementAmbiguousError:
    logging.error("Foram encontrados botões duplicados. O filtro found_index falhou em isolar o botão correto.")
except PywinautoTimeoutError:
    logging.error("Tempo esgotado aguardando o botão aparecer na tela. A internet pode estar lenta.")
except Exception as e:
    logging.exception("Um erro inesperado ocorreu durante a interação com os botões.")

logging.info("--- Automação finalizada ---")