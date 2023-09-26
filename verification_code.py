import re
from imap_tools import MailBox, AND, OR
from settings import get_email_credentials

EMAIL, EMAIL_PASSWORD = get_email_credentials()

def get_linkedin_verification_code():
    with MailBox('outlook.office365.com').login(username=EMAIL, password=EMAIL_PASSWORD, initial_folder="INBOX") as mailbox:
    
        for email in mailbox.fetch(AND(OR(subject="Este"), from_="security-noreply@linkedin.com"), reverse=True): #Melhorar método de busca dos e-mail, principalmente o valor passado para subject

            latest_linkedin_email = email

            break

    unhandled_verification_code = re.findall(r'\d+', latest_linkedin_email.subject)

    verification_code = ''.join(unhandled_verification_code)

    return verification_code