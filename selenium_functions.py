from time import sleep

def connect(driver, count):
    """
    count = Quantidade de vezes que o botão conectar será apertado
    ------------------------------------------------------------
    Procurar pelo botão "conectar" e o botão "avançar". Se o botão conectar não estiver na tela, procurar pelo botão avançar.
    Se o botão avançar não estiver na tela ainda, rolar e repetir o processo.
    """
    n = 0
    while True:
        print("ciclo while entrado")
        nav = driver
        botoes_conectar = nav.find_elements('xpath', '//*[contains(@class, "artdeco-button") and .//span[text()="Conectar"]]')
        
        print(f'{len(botoes_conectar)} botoes conectar encontrados')

        for botao in botoes_conectar:
            botao.click()
            n += 1
            sleep(0.3)

            if n == count:
                return
            
        nav.find_element('xpath', '//*[contains(@class, "artdeco-button") and .//span[text()="Avançar"]]').click()
        