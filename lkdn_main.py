from lkdn_actions import lkdn_follow, lkdn_msg_new_connections
from selenium_functions import define_chrome_driver
from os import system
import platform

def main(driver=None, email=None, password=None):
    print('-'*60)
    opt = int(input(\
'''Digite uma das opções:
(1) -> Conectar com pessoas no linkedin
(2) -> Aceitar novos convites e enviar mensagem de boas-vindas
(0) -> Encerrar o programa
'''))
    print('-'*60)

    if opt == 1:
        if email is None and password is None:
            email = input("Digite seu email (o email será usado apenas na automação): ")
            password = input("Digite sua senha (a senha será usada apenas na automação): ")

        business = None
        text = input("Digite o texto da barra de pesquisa (ex: 'analista de dados', 'tech recruiter'): ")

        business_ask = int(input("Digite 1 se você quer filtrar por alguma empresa, ou digite 0 para não filtrar por nenhuma empresa: "))
        if business_ask == 1:
            business = input("Digite o nome da empresa que você quer filtrar (ex: 'google', 'facebook'): ")

        count = int(input("Digite a quantidade de pessoas que você quer se conectar: "))

        while count <= 0:
            print("Digite uma contagem maior que 0\n")
            count = int(input("Digite a quantidade de pessoas que você quer se conectar: "))

        if driver is None:
            driver = define_chrome_driver()

        lkdn_follow(text, driver, count, email, password, business)

    elif opt == 2:
        if email is None and password is None:
            email = input("Digite seu email (o email será usado apenas na automação): ")
            password = input("Digite sua senha (a senha será usada apenas na automação): ")
        
        if driver is None:
            driver = define_chrome_driver()

        lkdn_msg_new_connections(driver, email, password)

    else:
        if email is None and password is None:
            email = input("Digite seu email (o email será usado apenas na automação): ")
            password = input("Digite sua senha (a senha será usada apenas na automação): ")

        if driver is not None: driver.quit()
        exit()

    #limpar()
    main(driver, email, password)

def limpar():
    if (platform.system() == 'Windows'):
        system('cls')
    if (platform.system() == 'Linux'):
        system('clear')

if __name__ == "__main__":
    main()
