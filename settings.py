import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

def get_linkedin_credentials():
    LINKEDIN_EMAIL = os.environ.get("EMAIL")
    LINKEDIN_PASSWORD = os.environ.get("LINKEDIN_PASSWORD")

    return (LINKEDIN_EMAIL, LINKEDIN_PASSWORD)


def get_email_credentials():
    EMAIL = os.environ.get("EMAIL")
    EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

    return (EMAIL, EMAIL_PASSWORD)

