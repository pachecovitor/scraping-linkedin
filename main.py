from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from login import login
from search import search_companie_occupation_area

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", False)
options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

teste = login(driver=driver)
teste2 = search_companie_occupation_area(driver=driver,occupation_area="celulose")