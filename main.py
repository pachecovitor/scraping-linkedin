from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from login import login
from search import search_companie_occupation_area, get_number_of_pages, get_companies_link
from company import get_employees, get_company_information


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", False)
options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

teste = login(driver=driver)
teste2 = get_company_information(driver=driver, linkedin_url='https://www.linkedin.com/company/dynamox/')
print(teste2)

'''teste2 = get_employees(driver=driver, linkedin_url='https://www.linkedin.com/company/dynamox/')
print(teste2)'''

#teste2 = search_companie_occupation_area(driver=driver,occupation_area="celulose")
#pages = get_number_of_pages(driver=driver)

#get_companies_link(driver=driver,total_pages=pages,occupation_area="celulose")