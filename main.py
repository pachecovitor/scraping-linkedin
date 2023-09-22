import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from settings import get_linkedin_credentials

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service,options=options)

VERIFY_LOGIN_ID = "global-nav__primary-link"
REMEMBER_PROMPT = 'remember-me-prompt__form-primary'

def page_has_loaded(driver):
    page_state = driver.execute_script('return document.readyState;')
    return page_state == 'complete'

def login(driver, cookie = None, timeout= 10):
    if cookie is not None:
        return _login_with_cookie(driver, cookie)
    
    LINKEDIN_EMAIL, LINKEDIN_PASSWORD = get_linkedin_credentials()

    driver.get("https://www.linkedin.com/login")
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
  
    email_elem = driver.find_element(By.ID,"username")
    email_elem.send_keys(LINKEDIN_EMAIL)
  
    password_elem = driver.find_element(By.ID,"password")
    password_elem.send_keys(LINKEDIN_PASSWORD)
    password_elem.submit()
  
    if driver.current_url == 'https://www.linkedin.com/checkpoint/lg/login-submit':
        remember = driver.find_element(By.ID, REMEMBER_PROMPT)
        if remember:
            remember.submit()
  
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, VERIFY_LOGIN_ID)))
  
def _login_with_cookie(driver, cookie):
    driver.get("https://www.linkedin.com/login")
    driver.add_cookie({
      "name": "li_at",
      "value": cookie
    })

teste = login(driver)