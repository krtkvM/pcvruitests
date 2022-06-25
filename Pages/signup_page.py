from Pages.base_page import BasePage
from locators import SignupPageLocators


class SignupPage(BasePage):

    def enter_name(self, text):
        user_email = self.browser.find_element(*SignupPageLocators.USER_NAME)
        user_email.send_keys(text)

    def enter_surname(self, text):
        user_surname = self.browser.find_element(*SignupPageLocators.USER_SURNAME)
        user_surname.send_keys(text)

    def enter_email(self, text):
        user_email = self.browser.find_element(*SignupPageLocators.USER_EMAIL)
        user_email.send_keys(text)

    def enter_phonenumber(self, text):
        user_phonenumber = self.browser.find_element(*SignupPageLocators.USER_PHONENUMBER)
        user_phonenumber.send_keys(text)

    def enter_password(self, text):
        user_password = self.browser.find_element(*SignupPageLocators.USER_PASSWORD)
        user_password.send_keys(text)

    def enter_tenant_name(self, text):
        user_tenant_name = self.browser.find_element(*SignupPageLocators.USER_TENANT_NAME)
        user_tenant_name.send_keys(text)

    def press_signup_button(self):
        signup_button = self.browser.find_element(*SignupPageLocators.SIGN_UP_BUTTON)
        signup_button.click()
