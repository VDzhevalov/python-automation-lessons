import allure

from lesson_30.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from lesson_30.pages.garage_page import GaragePage


class RegistrationForm(BasePage):

    @allure.step
    def get_name_input_field(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "signupName")))

    @allure.step
    def get_last_name_input_field(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "signupLastName")))

    @allure.step
    def get_email_input_field(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "signupEmail")))

    @allure.step
    def get_password_input_field(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "signupPassword")))

    @allure.step
    def get_reenter_password_input_field(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "signupRepeatPassword")))

    @allure.step
    def get_register_button(self):
        return self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary'][normalize-space()='Register']")))

    @allure.step
    def click_register_button(self) -> GaragePage:
        self.get_register_button().click()
        return GaragePage(self.driver)