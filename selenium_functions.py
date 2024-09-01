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


def define_chrome_driver():        
    servico = Service(ChromeDriverManager().install())

    opcoes = webdriver.ChromeOptions()
    opcoes.add_argument('user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data')
    opcoes.add_experimental_option('detach', True)

    navegador = webdriver.Chrome(service=servico, options=opcoes)
    
    return navegador


def connect(driver, count):
    """
    count = Quantidade de vezes que o botão conectar será apertado
    ------------------------------------------------------------
    Procurar pelo botão "conectar" e o botão "avançar". Se o botão conectar não estiver na tela, procurar pelo botão avançar.
    Se o botão avançar não estiver na tela ainda, rolar e repetir o processo.
    """
    if count <= 0:
        return
    
    n = 0
    while True:
        botoes_conectar = []
        try:
            botoes_conectar = WebDriverWait(driver, 4).until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(@class, "artdeco-button") and .//span[text()="Conectar"]]')))
        except:
            print("Nenhum botão conectar encontrado!")
            
        print(f"count = {count}")

        for botao in botoes_conectar:
        
            botao.click()
            n += 1
            print(f"Total de botões conectados até o momento: {n}")
            
            if WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '*//span[text()="Adicionar nota"]'))):
                driver.find_element('xpath', '*//button[@aria-label="Enviar sem nota"]').click()

            try:
                driver.find_element('xpath', '//button[@aria-label="Entendi"]').click()
            except:
                pass

            sleep(randint(1,4))

            if botao in WebDriverWait(driver, randint(2,4)).until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(@class, "artdeco-button") and .//span[text()="Conectar"]]'))):
                botao.click()
                sleep(randint(1,3))

                if WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '*//span[text()="Adicionar nota"]'))):
                    driver.find_element('xpath', '*//button[@aria-label="Enviar sem nota"]').click()

            if n == count:
                print(f"{n} botões conectar foram clicados!")
                print("Encerrando função conectar...")
                return

        sleep(randint(1,3))

        if len(driver.find_elements('xpath', '//*[contains(@class, "artdeco-button") and .//span[text()="Conectar"]]')) > 0:
                continue

        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()

        try:
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Avançar"]]'))).click()
        except:
            sleep(randint(1,3))
            ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
            try:
                WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Avançar"]]'))).click()
            except:
                print("ERRO: Nenhum botão 'avançar' encontrado.")
                print(f"{n} botões conectar foram clicados!")
                print("Encerrando função conectar...")
                return # Caso não tenha mais nenhum botão avançar

        sleep(randint(1,3))
        print("Lendo próxima página")


def new_connection_msg(navegador):
    texto = \
"""Opa, ! Tudo certo?

Valeu por aceitar minha conexão aqui no LinkedIn. Massa ter você na minha rede! Tomara que a gente possa trocar uma ideia e quem sabe rolar alguma parceria que dê um up nas nossas carreiras.

Abraço,

Iago Flávio."""

    nome = WebDriverWait(navegador, 5).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@class, "profile-card")]/span'))).text

    return texto[:5] + nome.split()[0] + texto[5:]


        