#%%
from selenium_functions import define_chrome_options
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import selenium_functions

def lkdn_follow(navegador):
    #%%      
    # Entrar no linkedin
    navegador.get('https://br.linkedin.com/')

    # Buscar por analista de dados e apertar enter
    navegador.find_element('xpath', '//*[@id="global-nav-typeahead"]/input').send_keys('analista de dados')
    webdriver.ActionChains(navegador).send_keys(Keys.ENTER).perform()

    sleep(2)
    #%%
    # Apertar o botão pessoas
    WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "artdeco-pill") and text()="Pessoas"]'))).click()

    #%%
    # Apertar o botão empresas e filtrar
    WebDriverWait(navegador, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="searchFilter_currentCompany"]'))).click()
    sleep(1)
    navegador.find_element('xpath', '//*[contains(@class, "search-reusables__value-label") and .//.//.//span[text()="Data Mundo"]]').click()
    #%%
    # Apertar em buscar resultados
    navegador.find_elements('xpath', '//*[contains(@class, "artdeco-button") and .//span[text()="Exibir resultados"]]')[1].click()
    # %%
    # Executando função de conectar
    selenium_functions.connect(driver=navegador, count=15)

if __name__ == "__main__":
    #%%
    navegador = define_chrome_options()
    lkdn_follow(navegador)