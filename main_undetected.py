import undetected_chromedriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

opcoes = undetected_chromedriver.ChromeOptions()

opcoes.add_argument("--disable-geolocation")
opcoes.add_argument("--disable-notifications")

navegadorChrome = undetected_chromedriver.Chrome(
    options=opcoes, 
    use_subprocess=True,
    version_main=153
    )

navegadorChrome.get("https://det.sit.trabalho.gov.br/login?r=%2Fservicos")

espera = WebDriverWait(navegadorChrome, 10)

botao_entrar = espera.until( 
    expected_conditions.element_to_be_clickable((By.ID, "botao"))
)

botao_entrar.click()

botao_certificado = espera.until(
    expected_conditions.visibility_of_element_located((By.ID, "login-certificate"))
)

mouse = ActionChains(navegadorChrome)

mouse.move_to_element(botao_certificado).click().perform()

input("Finalizar? Enter: ")