from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def connect(driver, count):
    """
    count = Quantidade de vezes que o botão conectar será apertado
    ------------------------------------------------------------
    Procurar pelo botão "conectar" e o botão "avançar". Se o botão conectar não estiver na tela, procurar pelo botão avançar.
    Se o botão avançar não estiver na tela ainda, rolar e repetir o processo.
    """
    n = 0
    while True:
        print(f"n = {n}")
        print("ciclo while entrado")
        nav = driver
        botoes_conectar = nav.find_elements('xpath', '//*[contains(@class, "artdeco-button") and .//span[text()="Conectar"]]')
        
        print(f'{len(botoes_conectar)} botoes conectar encontrados')

        print("entrando ciclo for")
        for botao in botoes_conectar:
            
            botao.click()
            n += 1
            sleep(1)

            if nav.find_element('xpath', '*//span[text()="Adicionar nota"]'):
                nav.find_element('xpath', '*//button[@aria-label="Enviar sem nota"]').click()

            if n == count:
                return
        
        print("rolando a página")
        footer = nav.find_element(By.TAG_NAME, "footer")
        delta_y = footer.rect['y']
        print(f"delta_y = {delta_y}")

        # TODO: ActionChains.scroll_by_amount() missing 1 required positional argument: 'delta_y'
        ActionChains.scroll_by_amount(0, delta_y).perform()

        print("Esperando botão 'avançar' ser clicado")
        WebDriverWait(nav, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[.//span[text()="Avançar"]]'))).click()
        
        sleep(3)
        print("dormindo")
        