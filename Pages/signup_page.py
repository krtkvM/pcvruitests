from Pages.base_page import BasePage
from locators import SignupPageLocators


class SignupPage(BasePage):

    def enter_name(self, text):
        user_email = self.browser.find_element(*SignupPageLocators.USER_NAME)
        user_email.send_keys(text)
