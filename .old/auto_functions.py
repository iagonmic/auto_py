import pyautogui as pag
from time import sleep

## Versão PYAYTOGUI
def connect(count):
    """
    count = Quantidade de vezes que o botão conectar será apertado
    ------------------------------------------------------------
    Procurar pelo botão "conectar" e o botão "avançar". Se o botão conectar não estiver na tela, procurar pelo botão avançar.
    Se o botão avançar não estiver na tela ainda, rolar e repetir o processo.
    """
    n = 0
    while True:
        try:
            conectar_btn = pag.locateOnScreen('images/conectar_btn.png')
            print(conectar_btn)
        except:
            conectar_btn = None
            print(f"conectar_btn = {conectar_btn}")
        if conectar_btn is None:
            try:
                avancar_btn = pag.locateOnScreen('images/avancar_btn.png')
                print(avancar_btn)
            except:
                avancar_btn = None
                print(f"avançar_btn = {avancar_btn}")
            if avancar_btn is None:
                pag.scroll(-300)
                continue
            pag.click(avancar_btn)
            sleep(2)
            continue 
        for button in list(pag.locateAllOnScreen('images/conectar_btn.png')):
            print(f"button = {button}")
            pag.click(button)
            n += 1
            if n == count:
                return

def click(img_name):
    print(img_name)
    return pag.click(pag.locateOnScreen('images/' + img_name + '.png'))


