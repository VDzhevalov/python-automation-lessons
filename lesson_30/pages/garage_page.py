import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from lesson_30.pages.base_page import BasePage

class GaragePage(BasePage):

    @allure.step
    def get_fuel_expenses_button(self):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, "expenses")

    @allure.step
    def get_garage_button(self):
        return self.driver.find_element(By.XPATH, "//a[@routerlink='garage']")

    @allure.step
    def get_instructions_button(self):
        return self.driver.find_element(By.XPATH, "//a[@routerlink='instructions']")

    @allure.step
    def get_log_out_button(self):
        return self.driver.find_element(By.LINK_TEXT, "Log out")

    @allure.step
    def get_expenses_by_partial_link_text(self):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, "expenses")

    @allure.step
    def wait_until_expenses_present(self, timeout_seconds: float = 5):
        wait = WebDriverWait(self.driver, 5)
        wait.until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "expenses")))
        return self
