from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

def load_full_page(driver:str):
    
    full_html = driver.find_element(By.TAG_NAME, 'html')
    full_html.send_keys(Keys.END)

    time.sleep(2)