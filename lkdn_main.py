from lkdn_actions import lkdn_follow
from selenium_functions import define_chrome_options

def main():
    navegador = define_chrome_options()
    lkdn_follow(navegador)

if __name__ == "__main__":
    main()
