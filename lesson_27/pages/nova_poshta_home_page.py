from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class NPHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def open(self):
        host = self.driver.base_url
        # url = AuthHelper.with_basic_auth(host, "guest", "welcome2qauto")
        self.driver.get(host)
        return self

    def get_track_num_input_field_by_id(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "en")))

    def get_submit_track_search_button(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "np-number-input-desktop-btn-search-en")))

    def get_error_message(self):
        return self.wait.until(
            EC.presence_of_element_located((By.ID, "np-number-input-desktop-message-error-message")))