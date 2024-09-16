from lkdn_actions import lkdn_follow, lkdn_msg_new_connections
from selenium_functions import define_chrome_options

def main():
    driver = define_chrome_options()
    business = None
    text = 'analista de dados'
    count = 15 
        
    lkdn_follow(text, driver, count, business)
    lkdn_msg_new_connections(driver)
    
    driver.quit()
    quit()

if __name__ == "__main__":
    main()
