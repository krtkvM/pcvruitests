import time
from faker import Faker
from Pages.signup_page import SignupPage

fake = Faker()
fake_email = fake.email()


def test_signup(browser):
    link = "https://app.pcvr-stg.smartex-it.com/sign-up"
    signup_page = SignupPage(browser, link)
    signup_page.open()
    signup_page.enter_name(fake.name())
    time.sleep(5)
