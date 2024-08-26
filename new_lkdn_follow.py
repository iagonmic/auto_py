#%%
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import selenium_functions

#%%
servico = Service(ChromeDriverManager().install())

opcoes = webdriver.ChromeOptions()
opcoes.add_argument('user-data-dir=C:/Users/User/AppData/Local/Google/Chrome/User Data')
opcoes.add_experimental_option('detach', True)


navegador = webdriver.Chrome(service=servico, options=opcoes)

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
selenium_functions.connect(driver=navegador, count=2)
# %%
