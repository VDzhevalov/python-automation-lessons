from lesson_28.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from lesson_28.pages.garage_page import GaragePage


class RegistrationForm(BasePage):

    def get_name_input_field(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "signupName")))

    def get_last_name_input_field(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "signupLastName")))

    def get_email_input_field(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "signupEmail")))

    def get_password_input_field(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "signupPassword")))

    def get_reenter_password_input_field(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "signupRepeatPassword")))

    def get_register_button(self):
        return self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary'][normalize-space()='Register']")))

    def click_register_button(self) -> GaragePage:
        self.get_register_button().click()
        return GaragePage(self.driver)