#%%
from selenium_functions import new_connection_msg, eliminate_msg
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
def lkdn_follow(text: str, driver, count, business=None):
    # Entrar no linkedin
    driver.get('https://br.linkedin.com/')

    # Buscar por analista de dados e apertar enter
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="global-nav-typeahead"]/input'))).send_keys(str(text))
    ActionChains(driver).send_keys(Keys.ENTER).perform()

    sleep(randint(1,3))
    #%%
    # Apertar o botão pessoas
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "artdeco-pill") and text()="Pessoas"]'))).click()

    #%%
    # Apertar o botão empresas e filtrar
    if business is not None:
        business = str(business).title()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchFilter_currentCompany"]'))).click()
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f'//*[contains(@class, "search-reusables__value-label") and .//.//.//span[contains(text(), "{business}")]]'))).click()
        except:
            driver.find_element('xpath', '//input[@placeholder="Adicionar empresa"]').click()
            ActionChains(driver).send_keys(business).perform()
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, f'//div[contains(@id, "basic-result") and .//span[contains(., "{business}")]]'))).click()
    #%%
    # Apertar em buscar resultados
        WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(@class, "artdeco-button") and .//span[text()="Exibir resultados"]]')))[1].click()
    # %%
    # Executando função de conectar
    selenium_functions.connect(driver, count)


def lkdn_msg_new_connections(driver):
    #%% Entrar em minha rede
    driver.get('https://www.linkedin.com/mynetwork/invitation-manager/')

    eliminate_msg(driver)
    #%% Clicar nos botões aceitar
    try:
        botoes_aceitar = WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//button[contains(@aria-label, "Aceitar")]')))
        for aceitar_btn in botoes_aceitar:
            aceitar_btn.click()
            sleep(randint(1,3))
    except:
        pass

    driver.get('https://www.linkedin.com/mynetwork/invite-connect/connections/')
            
    # Ir em "gerenciar minhas conexões"

    #%% Realizar loop e enviar mensagem até que encontre uma pessoa que ainda não enviou
    for enviar_mensagem_btn in WebDriverWait(driver,5).until(EC.presence_of_all_elements_located((By.XPATH, '//button[contains(@aria-label, "Enviar mensagem")]'))):
        eliminate_msg(driver)
        # Clicar no botão enviar mensagem
        enviar_mensagem_btn.click()
        sleep(randint(1,3))

        # Exceção para caso seja passada a url incorreta no linkedin
        if 'https://www.linkedin.com/messaging' in driver.current_url:
            lkdn_msg_new_connections(driver)

        # Verificar se já existe alguma mensagem mandada antes
        if len(driver.find_elements('xpath', '//div[contains(@class, "msg-s-event")]')) != 0:
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            break

        # Receber texto de acordo com o usuário que está aparecendo na tela
        text = new_connection_msg(driver)
        copy(text)
        # Colar texto dentro da text_box do usuário a ser enviado mensagem
        
        text_box = driver.find_element('xpath', '//div[contains(@class, "msg-form__contenteditable")]')
        
        (ActionChains(driver)
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
        driver.find_element('xpath', '//button[contains(@class, "msg-form__send-button")]').click()

        # Verificar se mensagem foi enviada e fechar aba de mensagem atual
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "msg-s-event")]')))
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        except:
            # Exceção para mensagem não enviada
            try:
                WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Tente novamente")]'))).click()
                ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            except:
                pass
