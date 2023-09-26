import os
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def use_cookie():
    try:
        LINKEDIN_COOKIE = os.environ.get("LINKEDIN_TOKEN")
        return LINKEDIN_COOKIE
    except Exception as e:
        return None 


def get_cookie(driver):
    li_at_cookie = driver.get_cookie("li_at")

    if li_at_cookie:
        linkedin_token = li_at_cookie["value"]

    return linkedin_token

def save_cookie(cookie):
    load_dotenv()

    with open(".env","a") as env_file:
        env_file.write(f'LINKEDIN_TOKEN={cookie}\n')

    print("Cookie salvo")

def login_cookie(driver, cookie):
    driver.get("https://www.linkedin.com/login")
    driver.add_cookie({
      "name": "li_at",
      "value": cookie
    })
