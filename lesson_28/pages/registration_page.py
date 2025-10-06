from selenium.webdriver.common.by import By
from lesson_28.pages.base_page import BasePage


class RegistrationPage(BasePage):
    NAME_INPUT = (By.ID, "signupName")
    LAST_NAME_INPUT = (By.ID, "signupLastName")
    EMAIL_INPUT = (By.ID, "signupEmail")
    PASSWORD_INPUT = (By.ID, "signupPassword")
    REPEAT_PASSWORD_INPUT = (By.ID, "signupRepeatPassword")
    REGISTER_BUTTON = (By.XPATH, "//button[@type='button' and contains(text(),'Register')]")

    def enter_name(self, name):
        self.find_element(self.NAME_INPUT).send_keys(name)

    def enter_last_name(self, last_name):
        self.find_element(self.LAST_NAME_INPUT).send_keys(last_name)

    def enter_email(self, email):
        self.find_element(self.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.find_element(self.PASSWORD_INPUT).send_keys(password)

    def repeat_password(self, password):
        self.find_element(self.REPEAT_PASSWORD_INPUT).send_keys(password)

    def click_register_button(self):
        self.find_clickable_element(self.REGISTER_BUTTON).click()
