import pyautogui as pag
import time

pag.PAUSE = 0.3

# Abrir o chrome
pag.press('win')
pag.write('chrome')
pag.press('enter')

time.sleep(2)

# Entrar no linkedin
pag.write('br.linkedin.com')
pag.press('enter')

time.sleep(5)

# Clicar na barra e pesquisa e digitar 'analista de dados', depoisd dar enter
lkdn_search_bar = pag.locateOnScreen('images/lkdn_search_bar.png')
pag.click(lkdn_search_bar)
pag.write('analista de dados')
pag.press('enter')

# Localizar o botão 'pessoas'
