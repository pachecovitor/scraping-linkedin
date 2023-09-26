from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def search_companie_occupation_area(driver, occupation_area, timeout=10):
    driver.get(f'https://www.linkedin.com/search/results/companies/?keywords={occupation_area}&origin=SWITCH_SEARCH_VERTICAL')
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, "search-global-typeahead__input")))
    get_number_of_pages(driver=driver)

def get_number_of_pages(driver):
    pagination_ul = driver.find_element(By.CSS_SELECTOR, ".artdeco-pagination__pages.artdeco-pagination__pages--number")
    pagination_li_elements = pagination_ul.find_elements(By.TAG_NAME, "li")
    num_pages = len(pagination_li_elements)

    print(f"Número de páginas de paginação: {num_pages}")