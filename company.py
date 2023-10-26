import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def __parse_employee__(employee_raw, company_name:str) -> dict:

        try:
            employee_object = {}
            employee_object['employee_company'] = company_name
            employee_object['employee_name'] = (employee_raw.text.split("\n") or [""])[0].strip()
            employee_object['employee_designation'] = (employee_raw.text.split("\n") or [""])[3].strip()
            employee_object['employee_linkedin_url'] = employee_raw.find_element(By.TAG_NAME, "a").get_attribute("href")

            return employee_object
        except Exception as e:
            return None

def get_employees(driver:str, linkedin_url:str, wait_time:int=10,) -> list:
    total = []
    list_css = "list-style-none"
    next_xpath = '//button[@aria-label="Next"]'

    try:
        see_all_employees = driver.find_element(By.XPATH,'//a[@data-control-name="topcard_see_all_employees"]')
    except:
        pass
    driver.get(os.path.join(linkedin_url, "people"))

    _ = WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@dir="ltr"]')))
     
    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight*3/4));")
    time.sleep(1)
     
    results_list = driver.find_element(By.CLASS_NAME, list_css)
    results_li = results_list.find_elements(By.TAG_NAME, "li")
    company = driver.find_element(By.XPATH,'//span[@dir="ltr"]')
    for res in results_li:
        total.append(__parse_employee__(employee_raw=res, company_name=company.text))
    def is_loaded(previous_results):
        loop = 0
        driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight));")
        results_li = results_list.find_elements(By.TAG_NAME, "li")
        while len(results_li) == previous_results and loop <= 5:
            time.sleep(1)
            driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight));")
            results_li = results_list.find_elements(By.TAG_NAME, "li")
            loop += 1
        return loop <= 5
     
    def get_data(previous_results):
        results_li = results_list.find_elements(By.TAG_NAME, "li")
        company = driver.find_element(By.XPATH,'//span[@dir="ltr"]')
        for res in results_li[previous_results:]:
            total.append(__parse_employee__(employee_raw=res, company_name=company))
     
    results_li_len = len(results_li)
    while is_loaded(results_li_len):
        try:
            driver.find_element(By.XPATH,next_xpath).click()
        except:
            pass
        _ = WebDriverWait(driver, wait_time).until(EC.presence_of_element_located((By.CLASS_NAME, list_css)))

        driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight/2));")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight*2/3));")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight*3/4));")
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, Math.ceil(document.body.scrollHeight));")
        time.sleep(1)

        get_data(results_li_len)
        results_li_len = len(total)
    return total

def get_company_information(driver:str, linkedin_url:str) -> dict:

    driver.get(os.path.join(linkedin_url, "about"))

    WebDriverWait(driver, 3).until(EC.presence_of_all_elements_located((By.XPATH, '//span[@dir="ltr"]')))

    company_info = {}
    
    #elements = driver.find_elements(By.XPATH,'//dl//dt')
    #elements2 = driver.find_elements(By.XPATH,'//dl//dd')

    company_info['company_name'] = driver.find_element(By.XPATH,'//span[@dir="ltr"]').text
    company_info['company_about_us'] = driver.find_element(By.XPATH,'//p[@class="break-words white-space-pre-wrap t-black--light text-body-medium"]').text.strip()
    company_info['specialties'] = driver.find_element(By.XPATH,'//dd[@class="mb4 t-black--light text-body-medium" and @dir="ltr"]').text.strip()
    company_info['website'] = driver.find_element(By.XPATH,'//dd[@class="link-without-visited-state" and @dir="ltr"]').text.strip()
    company_info['headquarters'] = driver.find_element(By.CSS_SELECTOR, ".mb4.t-black--light.text-body-medium").text.strip()
    company_info['industry'] = driver.find_element(By.CLASS_NAME, "industry").text.strip()
    company_info['company_size'] = driver.find_element(By.CLASS_NAME, "company-size").text.strip()
    company_info['company_type'] = ''
    company_info['founded'] = ''

    return company_info