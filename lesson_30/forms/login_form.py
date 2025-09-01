import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from lesson_30.forms.registration_form import RegistrationForm
from lesson_30.pages.base_page import BasePage


class LoginForm(BasePage):

    @allure.step
    def get_email_input_field(self):
        return self.wait.until(
            EC.presence_of_element_located((By.NAME, "email")))

    @allure.step("set_email: {email}")
    def set_email(self, email):
        self.get_email_input_field().send_keys(email)

    @allure.step
    def get_password_input_field(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "signinPassword")))

    @allure.step("set_password")
    def set_password(self, password):
        self.get_password_input_field().send_keys(password)

    @allure.step
    def get_close_button(self):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Close']")))

    @allure.step
    def get_login_button(self):
        return self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary'][normalize-space()='Login']")))

    @allure.step
    def click_login_button(self):
        self.get_login_button().click()

    @allure.step
    def get_registration_link(self):
        return self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-link'][normalize-space()='Registration']")))

    @allure.step
    def click_registration_link(self) -> RegistrationForm:
        self.get_registration_link().click()
        return RegistrationForm(self.driver)