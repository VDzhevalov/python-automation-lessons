import os
import tempfile

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from lesson_30.forms.login_form import LoginForm
from lesson_30.pages.garage_page import GaragePage
from lesson_30.pages.home_page import HomePage


@pytest.fixture(scope='session')
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-gpu")

    user_data_dir = os.environ.get("CHROME_USER_DATA_DIR") or tempfile.mkdtemp(prefix="chrome-profile-")
    opts.add_argument(f"--user-data-dir={user_data_dir}")

    drv = webdriver.Chrome(options=opts)
    drv.set_window_size(1920, 1080)
    drv.base_url = "https://qauto2.forstudy.space"

    yield drv
    drv.quit()

@pytest.fixture
@allure.step
def open_home_page(driver):
    def _open_home_page():
        HomePage(driver).open()
    return _open_home_page


@pytest.fixture
@allure.step
def open_sign_in_page(driver):
    def _open_sign_in_page():
        HomePage(driver).click_sign_in_button()
    return _open_sign_in_page

@pytest.fixture
@allure.step
def sign_in(driver):
    def _sign_in():
        login_form = LoginForm(driver)
        # login_form.get_password_input_field().send_keys("12345678aA")
        login_form.set_password("12345678aA")
        # login_form.get_email_input_field().send_keys("123_aa@test.com")
        login_form.set_email("123_aa@test.com")
        # login_form.get_login_button().click()
        login_form.click_login_button()
    return _sign_in

@pytest.fixture
@allure.step
def check_successful_login(driver):
    def _check_successful_login():
        page = GaragePage(driver).wait_until_expenses_present(timeout_seconds=5)
        return (
            page.get_fuel_expenses_button(),
            page.get_instructions_button(),
            page.get_garage_button(),
        )
    return _check_successful_login