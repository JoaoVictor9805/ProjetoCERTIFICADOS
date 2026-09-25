from selenium.common import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.edge.options import Options

import time

# ================
# Etapa 00 - Configurando
# ================

opcoes = Options()

preferencias = {
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 2,
}

opcoes.add_experimental_option("prefs", preferencias)

# ================
# Etapa 01 - Abrindo navegador
# ================

navegadorEdge = webdriver.Edge(options=opcoes)

navegadorEdge.get("https://det.sit.trabalho.gov.br/login?r=%2Fservicos")

# Força aprovação da geolocalização por baixo dos panos
navegadorEdge.execute_cdp_cmd(
    "Browser.grantPermissions",
    {
        "origin": "https://sso.acesso.gov.br",
        "permissions": ["geolocation"]
    }
)

espera = WebDriverWait(navegadorEdge, 10)

botao_entrar = espera.until( 
    expected_conditions.element_to_be_clickable((By.ID, "botao"))
)

botao_entrar.click()

botao_certificado = espera.until(
    expected_conditions.visibility_of_element_located((By.ID, "login-certificate"))
)

mouse = ActionChains(navegadorEdge)

mouse.move_to_element(botao_certificado).click().perform()

input("Finalizar? Enter: ")