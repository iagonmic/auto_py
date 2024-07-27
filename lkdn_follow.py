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

time.sleep(5)

# Localizar o botão 'pessoas' e clicar
pessoas_btn = pag.locateOnScreen('images/pessoas_btn.png')
pag.click(pessoas_btn)

time.sleep(2)

# Localizar o botão 'empresa atual' e clicar
empresa_atual_btn = pag.locateOnScreen('images/empresa_atual_btn.png')
pag.click(empresa_atual_btn)

time.sleep(0.5)

# Filtrar por empresa == 'Data Mundo'
data_mundo_btn = pag.locateOnScreen('images/data_mundo_btn.png')
pag.click(data_mundo_btn)
exibir_resultados_btn = pag.locateOnScreen('images/exibir_resultados_btn.png')
pag.click(exibir_resultados_btn)
