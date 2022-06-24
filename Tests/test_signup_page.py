import time
from random import randint

from faker import Faker
from Pages.signup_page import SignupPage

fake = Faker()
fake_email = fake.email()

# rndmnumber = randint(1, 100000)

def test_signup(browser):
    link = "https://app.pcvr-stg.smartex-it.com/sign-up"
    rndm_number = str(randint(1, 100000))

    signup_page = SignupPage(browser, link)
    signup_page.open()
    signup_page.enter_name(fake.name())
    signup_page.enter_surname("qa")
    signup_page.enter_email("mkrtkv2@gmail.com")
    signup_page.enter_phonenumber("1234567890")
    signup_page.enter_password("qwe123")
    signup_page.enter_tenant_name("autoqa" + rndm_number)
    time.sleep(5)
