import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def __parse_employee__(employee_raw):

        try:
            employee_object = {}
            employee_object['name'] = (employee_raw.text.split("\n") or [""])[0].strip()
            employee_object['designation'] = (employee_raw.text.split("\n") or [""])[3].strip()
            employee_object['linkedin_url'] = employee_raw.find_element(By.TAG_NAME, "a").get_attribute("href")

            return employee_object
        except Exception as e:
            return None


def get_employees(driver, wait_time=10):
    total = []
    list_css = "list-style-none"
    next_xpath = '//button[@aria-label="Next"]'
    linkedin_url = 'https://www.linkedin.com/company/dynamox/'

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
    for res in results_li:
        total.append(__parse_employee__(res))
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
        for res in results_li[previous_results:]:
            total.append(__parse_employee__(res))
     
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

