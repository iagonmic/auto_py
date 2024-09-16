from pyautogui import write, press
from time import sleep
from auto_functions import click, connect

PAUSE = 0.3

# Abrir o chrome
press('win')
write('chrome')
sleep(0.5)
press('enter')

sleep(2)

# Entrar no linkedin
write('br.linkedin.com')
press('enter')

sleep(5)

# Clicar na barra de pesquisa e digitar 'analista de dados', depois dar enter
click('lkdn_search_bar')
write('analista de dados')
press('enter')

sleep(5)

# Localizar o botão 'pessoas' e clicar
click('pessoas_btn')
sleep(3)

# Localizar o botão 'empresa atual' e clicar
click('empresa_atual_btn')
sleep(0.5)

# Filtrar por empresa == 'Data Mundo'
click('data_mundo_btn')
click('exibir_resultados_btn')

sleep(2)

'''
Procurar pelo botão "conectar" e o botão "avançar". Se o botão conectar não estiver na tela, procurar pelo botão avançar.
Se o botão avançar não estiver na tela ainda, rolar e repetir o processo.
'''
connect(15)