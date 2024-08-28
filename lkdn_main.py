from lkdn_actions import lkdn_follow, lkdn_msg_new_connections
from selenium_functions import define_chrome_options

def main():
    navegador = define_chrome_options()
    lkdn_follow(navegador)
    lkdn_msg_new_connections(navegador)

if __name__ == "__main__":
    main()
