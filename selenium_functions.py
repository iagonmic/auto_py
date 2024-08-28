from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random import randint


def define_chrome_options():        
    servico = Service(ChromeDriverManager().install())

    opcoes = webdriver.ChromeOptions()
    opcoes.add_argument('user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data')
    opcoes.add_experimental_option('detach', True)

    navegador = webdriver.Chrome(service=servico, options=opcoes)
    
    return navegador

def connect(nav, count):
    """
    count = Quantidade de vezes que o botão conectar será apertado
    ------------------------------------------------------------
    Procurar pelo botão "conectar" e o botão "avançar". Se o botão conectar não estiver na tela, procurar pelo botão avançar.
    Se o botão avançar não estiver na tela ainda, rolar e repetir o processo.
    """
    n = 0
    while True:
        
        botoes_conectar = nav.find_elements('xpath', '//*[contains(@class, "artdeco-button") and .//span[text()="Conectar"]]')
        
        print(f'{len(botoes_conectar)} botoes conectar encontrados')

        for botao in botoes_conectar:
            
            botao.click()
            n += 1
            sleep(randint(1,3))
            print(f"n = {n}")

            if nav.find_element('xpath', '*//span[text()="Adicionar nota"]'):
                nav.find_element('xpath', '*//button[@aria-label="Enviar sem nota"]').click()

            if n == count:
                return
            
        sleep(randint(1,3))
        ActionChains(nav).send_keys(Keys.PAGE_DOWN).perform()
        print("Esperando botão 'avançar' ser clicado")

        try:
            WebDriverWait(nav, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Avançar"]]'))).click()
        except:
            sleep(randint(1,3))
            ActionChains(nav).send_keys(Keys.PAGE_DOWN).perform()
            WebDriverWait(nav, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Avançar"]]'))).click()

        sleep(randint(1,3))
        print("dormindo")

def new_connection_msg(navegador):
    texto = \
"""Opa, ! Tudo certo?

Valeu por aceitar minha conexão aqui no LinkedIn. Massa ter você na minha rede! Tomara que a gente possa trocar uma ideia e quem sabe rolar alguma parceria que dê um up nas nossas carreiras.

Abraço,

Iago Flávio."""

    nome = WebDriverWait(navegador, 5).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@class, "profile-card")]/span'))).text

    return texto[:5] + nome.split()[0] + texto[5:]


        