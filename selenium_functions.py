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

class Button:
    
    def __init__(self, element, clicked:bool=False):
        self.element = element
        self.clicked = clicked

    def click_button(self) -> bool:
        self.element.click()
        self.clicked = True
        return True

    def click_button_by_xpath(self, driver, xpath):
        try:
            WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, f'{xpath}'))).click()
            self.clicked = True
            return True
        except:
            return False

    def find_button_by_xpath(self, driver, xpath):
        try:
            element = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, f'{xpath}')))
            return element
        except:
            return None
        
def button_list(list):
    for i, element in enumerate(list):
        list[i] = Button(element)
    
    return list


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
    botoes_conectar = []
    while True:
        eliminate_msg(driver)
        try:
            # Resolver problema de botão clicado ou não, rastrear com POO
            if len(botoes_conectar) == 0:
                botoes_conectar = button_list(WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((
                    By.XPATH, '//*[contains(@class, "artdeco-button") and .//span[text()="Conectar"]]'))))
                
            print(f'primeiro botoes_conectar: {botoes_conectar}\no tamanho atual de botoes_conectar é {len(botoes_conectar)}\n')

            # remover botoes que já foram clicados ao voltar para cá
            for botao in botoes_conectar:

                if botao.clicked == True:
                    botoes_conectar.remove(botao)
                    print(f'Botão clicado encontrado! o botão removido foi {botao} botoes_conectar: {botoes_conectar}\no tamanho atual de botoes_conectar é {len(botoes_conectar)}\n')
        except:
            print("Nenhum botão conectar encontrado!")

        for botao in botoes_conectar:
            print(f'botao atual = {botao}')

            pending_invite_msg_close(driver)

            # Except: Por algum motivo, ele não retira todos os botoes clicados e permanece voltando para cá
            try:
                botao.click_button()
            except Exception as e:
                template = "Uma exceção do tipo {0} ocorreu. Argumentos:\n{1!r}"
                message = template.format(type(e).__name__, e.args)
                print(message)
                botoes_conectar = []
                break

            n += 1

            print(f"Total de botões conectados até o momento: {n}")

            # exceção para ignorar o retirar convite caso clique duas vezes
            pending_invite_msg_close(driver)

            # exceção após o clique do botão em convite personalizado            
            if botao.find_button_by_xpath(driver, '*//span[text()="Adicionar nota"]') is not None:
                botao.click_button_by_xpath(driver, '*//button[@aria-label="Enviar sem nota"]')

            try:
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//div[@data-test-modal-id="send-invite-modal"]')))
                driver.find_element('xpath', '//button[@aria-label="Fechar" and .//span[contains(@class, "artdeco-button")]]').click()
                n -= 1
                continue
            except:
                pass

            # limite mensal de convites
            try:
                driver.find_element('xpath', '//button[@aria-label="Entendi"]').click()
                botao.click_button()
            except:
                pass

            sleep(randint(1,3))

            # exceção para garantir o primeiro botão da lista
            new_temp_list = []
            try:
                new_temp_list = button_list(WebDriverWait(driver, randint(2,4)).until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(@class, "artdeco-button") and .//span[text()="Conectar"]]'))))
            except:
                pass
            
            if botao in botoes_conectar:
                print("botão está em botoes_conectar")

                if botao in new_temp_list:
                    print("botão está em new_temp_list")

                    botao.click_button()
                    sleep(randint(1,3))

                    try:
                        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '*//span[text()="Adicionar nota"]')))
                        driver.find_element('xpath', '*//button[@aria-label="Enviar sem nota"]').click()
                        continue
                    except:
                        pass
            
                
            # quebrar o ciclo for se n for atingido
            if n == count:
                print(f"{n} botões conectar foram clicados!")
                print("Encerrando função conectar...")
                return

        sleep(randint(1,3))

        if len(botoes_conectar) > 0:
            print("cheguei aqui no len")
            continue

        # desce a página até o final e clica no botão avançar
        ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()

        botao_avancar = None
        try:
            botao_avancar = Button(WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, '//button[.//span[text()="Avançar"]]'))))
        except:
            print("ERRO: Nenhum botão 'avançar' encontrado.")
            print(f"{n} botões conectar foram clicados!")
            print("Encerrando função conectar...")
            return # Caso não tenha mais nenhum botão avançar

        while True:
            pending_invite_msg_close(driver)

            if botao_avancar.clicked == True:
                botao_avancar = Button(WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, '//button[.//span[text()="Avançar"]]'))))

            if botao_avancar.find_button_by_xpath(driver, '//button[.//span[text()="Avançar"]]'):
                botao_avancar.click_button() # não registrar o clique aqui

            sleep(randint(2,4))

            if botao_avancar.find_button_by_xpath(driver, '//button[.//span[text()="Avançar"]]') is not botao_avancar.element:
                break

            ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform() # desce a página e clica no botão avançar novamente

        print("Lendo próxima página")


def new_connection_msg(navegador):
    texto = \
"""Opa, ! Tudo certo?

Valeu por aceitar minha conexão aqui no LinkedIn. Massa ter você na minha rede! Tomara que a gente possa trocar uma ideia e quem sabe rolar alguma parceria que dê um up nas nossas carreiras.

Abraço,

Iago Flávio."""

    nome = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@class, "profile-card")]/span'))).text

    return texto[:5] + nome.split()[0] + texto[5:]

def eliminate_msg(driver):
    list = []
    try:
        list = WebDriverWait(driver,2).until(EC.presence_of_all_elements_located((By.XPATH, '//button[contains(@class, "msg-overlay-bubble-header__control artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary")]')))
        if len(list) == 0:
            return
    except:
        pass
    
    for close_button in list:
        close_button.click()
        sleep(randint(1,2))

def pending_invite_msg_close(driver):
    try:
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.XPATH, '//button[contains(@class, artdeco-button) and .//span[contains(., "Retirar")]]')))
        driver.find_element('xpath', '//button[@aria-label="Fechar" and .//span[contains(@class, "artdeco-button")]]').click()
    except:
        pass