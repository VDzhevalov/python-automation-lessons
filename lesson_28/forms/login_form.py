from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from lesson_28.forms.registration_form import RegistrationForm
from lesson_28.pages.base_page import BasePage


class LoginForm(BasePage):

    def get_email_input_field(self):
        return self.wait.until(
            EC.presence_of_element_located((By.NAME, "email")))

    def get_password_input_field(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "signinPassword")))

    def get_close_button(self):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Close']")))

    def get_login_button(self):
        return self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary'][normalize-space()='Login']")))

    def get_registration_link(self):
        return self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-link'][normalize-space()='Registration']")))

    def click_registration_link(self) -> RegistrationForm:
        self.get_registration_link().click()
        return RegistrationForm(self.driver)