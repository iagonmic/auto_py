#%%
from selenium_functions import define_chrome_options, new_connection_msg
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random import randint
from time import sleep
from pyperclip import copy
import selenium_functions

#%%
def lkdn_follow(navegador):
    #%%      
    # Entrar no linkedin
    navegador.get('https://br.linkedin.com/')

    # Buscar por analista de dados e apertar enter
    navegador.find_element('xpath', '//*[@id="global-nav-typeahead"]/input').send_keys('analista de dados')
    ActionChains(navegador).send_keys(Keys.ENTER).perform()

    sleep(randint(1,3))
    #%%
    # Apertar o botão pessoas
    WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "artdeco-pill") and text()="Pessoas"]'))).click()

    #%%
    # Apertar o botão empresas e filtrar
    WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchFilter_currentCompany"]'))).click()
    sleep(randint(1,3))
    navegador.find_element('xpath', '//*[contains(@class, "search-reusables__value-label") and .//.//.//span[text()="Data Mundo"]]').click()
    #%%
    # Apertar em buscar resultados
    navegador.find_elements('xpath', '//*[contains(@class, "artdeco-button") and .//span[text()="Exibir resultados"]]')[1].click()
    # %%
    # Executando função de conectar
    selenium_functions.connect(driver=navegador, count=15)

def lkdn_msg_new_connections(navegador):
    #%% Entrar em minha rede
    navegador.get('https://www.linkedin.com/mynetwork/')

    #%% Clicar no botão de visualizar se existir
    if WebDriverWait(navegador, 5).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@aria-label, "Visualizar")]'))):
        navegador.find_element('xpath', '//a[contains(@aria-label, "Visualizar")]').click()
        
        #%% Clicar nos botões aceitar
        for aceitar_btn in navegador.find_elements('xpath', '//button[contains(@aria-label, "Aceitar")]'):
            sleep(randint(1,3))
            aceitar_btn.click()

    #%% Ir em "gerenciar minhas conexões"
    navegador.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')

    #%% Realizar loop e enviar mensagem até que encontre uma pessoa que ainda não enviou
    for enviar_mensagem_btn in navegador.find_elements('xpath', '//button[contains(@aria-label, "Enviar mensagem")]')[3:]:
        # Clicar no botão enviar mensagem
        enviar_mensagem_btn.click()
        sleep(randint(1,3))

        # Verificar se já existe alguma mensagem mandada antes
        if len(navegador.find_elements('xpath', '//div[contains(@class, "msg-s-event")]')) != 0:
            break
        # Receber texto de acordo com o usuário que está aparecendo na tela
        text = new_connection_msg(navegador)
        copy(text)
        # Colar texto dentro da text_box do usuário a ser enviado mensagem
        
        text_box = navegador.find_element('xpath', '//div[contains(@class, "msg-form__contenteditable")]')
        
        (ActionChains(navegador)
            .click(text_box)
            .key_down(Keys.CONTROL)
            .send_keys('a')
            .key_up(Keys.CONTROL)
            .send_keys(Keys.DELETE)
            .key_down(Keys.CONTROL)
            .send_keys('v')
            .key_up(Keys.CONTROL)
            .perform()
            )
        
        sleep(randint(1,3))
        # Enviar mensagem
        navegador.find_element('xpath', '//button[contains(@class, "msg-form__send-button")]').click()

        # Verificar se mensagem foi enviada e fechar aba de mensagem atual
        while len(navegador.find_elements('xpath', '//div[contains(@class, "msg-s-event")]')) == 0:
            sleep(1)
        
        ActionChains(navegador).send_keys(Keys.ESCAPE).perform()
        
#%%
if __name__ == "__main__":
    #%%
    navegador = define_chrome_options()
    #%%
    lkdn_follow(navegador)
    #%%
    lkdn_msg_new_connections(navegador)