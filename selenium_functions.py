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
            print("entrando ciclo for")
            botao.click()
            n += 1
            sleep(1)

            if n == count:
                return
        
        print("clicando em mudado")
        # Problema: não está encontrando o botão avançar
        nav.find_element('xpath', '//*[@aria-label="Avançar"]').click()
        sleep(3)
        print("dormindo")
        