import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from support import load_full_page

def search_companie_occupation_area(driver, occupation_area, timeout=10):
    driver.get(f'https://www.linkedin.com/search/results/companies/?keywords={occupation_area}&origin=SWITCH_SEARCH_VERTICAL')
    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CLASS_NAME, "search-global-typeahead__input")))

def get_number_of_pages(driver):

    load_full_page(driver=driver)

    pages = driver.find_elements(By.XPATH, '//ul[@class="artdeco-pagination__pages artdeco-pagination__pages--number"]/li')
    num_pages = int(pages[-1].text)

    return num_pages

def get_companies_link(driver, total_pages, occupation_area):

    companies_link = []

    for page in range(1, total_pages):

        driver.get(f'https://www.linkedin.com/search/results/companies/?keywords={occupation_area}&origin=SWITCH_SEARCH_VERTICAL&page={page}')
        load_full_page(driver=driver)

        elements = driver.find_elements(By.XPATH, '//ul[@class="reusable-search__entity-result-list list-style-none"]//li/div/div/div[2]/div[1]/div[1]/div/span/span/a')

        for element in elements:
            href = element.get_attribute('href')
            companies_link.append(href)
            print(href)
    return companies_link