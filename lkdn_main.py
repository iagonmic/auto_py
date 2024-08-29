from lkdn_actions import lkdn_follow, lkdn_msg_new_connections
from selenium_functions import define_chrome_driver

def main(driver=None):
    print('-'*60)
    opt = int(input(\
'''Digite uma das opções:
(1) -> Conectar com pessoas no linkedin
(2) -> Aceitar novos convites e enviar mensagem de boas-vindas
(0) -> Encerrar o programa
'''))
    print('-'*60)

    if opt == 1:
        business = None
        text = input("Digite o texto da barra de pesquisa (ex: 'analista de dados', 'tech recruiter'): ")
        business_ask = int(input("Digite 1 se você quer filtrar por alguma empresa, ou digite 0 para não filtrar por nenhuma empresa: "))
        count = int(input("Digite a quantidade de pessoas que você quer se conectar: "))

        if business_ask == 1:
            business = input("Digite o nome da empresa que você quer filtrar (ex: 'data mundo')")

        if driver is None:
            driver = define_chrome_driver()
            
        lkdn_follow(text, driver, count)

    elif opt == 2:
        if driver is None:
            driver = define_chrome_driver()

        lkdn_msg_new_connections(driver)

    else:
        exit()

    main(driver)

if __name__ == "__main__":
    main()
