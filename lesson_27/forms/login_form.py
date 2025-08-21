from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginForm:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def get_email_input_field_by_name(self):
        return self.wait.until(
            EC.presence_of_element_located((By.NAME, "email")))

    def get_password_input_field_by_id(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "signinPassword")))

    def get_close_button(self):
        return self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Close']")))
