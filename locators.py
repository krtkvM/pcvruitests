from selenium.webdriver.common.by import By

class SignupPageLocators():
    USER_NAME = (By.XPATH,'//div[@class="auth__fields"]/div[1]/div/input')
    USER_SURNAME = (By.XPATH, '//div[@class="auth__fields"]/div[2]/div/input')
    USER_EMAIL = (By.XPATH, '//div[@class="auth__fields"]/div[3]/div/input')
    USER_PHONENUMBER = (By.XPATH, '//div[@class="auth__fields"]/div[4]/div/div[3]/input')
    USER_PASSWORD = (By.XPATH, '//input[@type="password"]')
    USER_TENANT_NAME = (By.XPATH,'//div[@class="auth__fields"]/div[6]/div/div/div/input')
    SIGN_UP_BUTTON = (By.XPATH, '//button[contains(@class,"auth__button")]')



