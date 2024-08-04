#%%
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
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
navegador.find_element('xpath', '//*[@id="search-reusables__filters-bar"]/ul/li[3]/button').click()


#%%
# Apertar o botão empresas e filtrar
navegador.find_element('xpath', '//*[@id="searchFilter_currentCompany"]').click()
navegador.find_element('xpath', '//*[@id="artdeco-hoverable-artdeco-gen-63"]/div[1]/div/form/fieldset/div[1]/ul/li[2]/label').click()
#%%
# Apertar em buscar resultados
exibir_resultados = navegador.find_elements('xpath', '//*[contains(@class, "artdeco-button") and .//span[text()="Exibir resultados"]]') 
exibir_resultados[1].click()
# %%
selenium_functions.connect(driver=navegador, count=15)
# %%
