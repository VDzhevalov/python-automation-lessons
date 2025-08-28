import allure
from selenium.webdriver.common.by import By

from lesson_30.forms.login_form import LoginForm
from lesson_30.helpers.auth_helper import AuthHelper
from lesson_30.pages.base_page import BasePage


class HomePage(BasePage):

    @allure.step
    def open(self):
        host = self.driver.base_url
        url = AuthHelper.with_basic_auth(host, "guest", "welcome2qauto")
        self.driver.get(url)
        return self

    # -------- getters (XPATH) --------
    @allure.step
    def get_about_button_by_xpath(self):
        return self.driver.find_element(By.XPATH, "//button[@appscrollto='aboutSection']")

    @allure.step
    def get_contacts_button_by_xpath(self):
        return self.driver.find_element(By.XPATH, "//button[text()='Contacts']")

    @allure.step
    def get_home_button_by_xpath(self):
        return self.driver.find_element(By.XPATH, "//a[normalize-space()='Home']")

    @allure.step
    def get_guest_login_button_by_xpath(self):
        return self.driver.find_element(By.XPATH, "//button[normalize-space()='Guest log in']")

    @allure.step
    def get_sign_up_button_by_xpath(self):
        return self.driver.find_element(
            By.XPATH, "//div[contains(@class,'header_right')]/button[2]"
        )

    # -------- getters (CSS) --------
    @allure.step
    def get_sign_up_button_by_css(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button.header_signin")

    @allure.step
    def get_sign_up_button_by_css_attr_ends(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button[class$='header_signin']")

    @allure.step
    def get_sign_in_button_by_complex_css(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div.header_right button.header_signin")

    @allure.step
    def get_sign_up_button_by_class_name(self):
        # еквівалент By.CLASS_NAME ("header_signin") — залишив як CSS для єдності
        return self.driver.find_element(By.CLASS_NAME, "header_signin")

    # -------- actions --------
    @allure.step
    def click_about_button(self):
        self.get_about_button_by_xpath().click()
        return self

    @allure.step
    def click_contacts_button(self):
        self.get_contacts_button_by_xpath().click()
        return self

    @allure.step
    def click_home_button(self):
        self.get_home_button_by_xpath().click()
        return self

    @allure.step
    def click_guest_login_button(self) -> LoginForm:
        self.get_guest_login_button_by_xpath().click()
        return LoginForm(self.driver)

    @allure.step
    def click_sign_up_button(self):
        self.get_sign_up_button_by_xpath().click()
        return self

    @allure.step
    def click_sign_in_button(self):
        self.get_sign_in_button_by_complex_css().click()
        return self
