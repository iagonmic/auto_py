from lkdn_actions import lkdn_follow, lkdn_msg_new_connections
from selenium_functions import define_chrome_options

def main():
    driver = define_chrome_options()
    while True:
        opt = int(input(\
'''Digite uma das opções para começar:
(1) -> Conectar com pessoas no linkedin
(2) -> Aceitar novos convites e enviar mensagem de boas 
(3) -> Encerrar o programa
'''))
        if opt == 1:
            text = input("Digite o texto da barra de pesquisa (ex: 'analista de dados', 'tech recruiter'): ")
            business_ask = int(input("Digite 1 se você quer filtrar por alguma empresa, ou digite 0 para não filtrar por nenhuma empresa: "))
            count = int(input("Digite a quantidade de pessoas que você quer se conectar: "))

            if business_ask == 1:
                business = input("Digite o nome da empresa que você quer filtrar (ex: 'data mundo')")
                lkdn_follow(text, driver, count, business)    
                
            lkdn_follow(text, driver, count)

        elif opt == 2:
            lkdn_msg_new_connections(driver)
        else:
            quit()

if __name__ == "__main__":
    main()
