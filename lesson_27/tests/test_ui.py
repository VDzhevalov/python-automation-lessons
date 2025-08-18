import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from lesson_27.forms.login_form import LoginForm
from lesson_27.pages.garage_page import GaragePage
from lesson_27.pages.home_page import HomePage
import time


@pytest.fixture(scope='function')
def driver():
    opts = Options()
    drv = webdriver.Chrome(options=opts)
    drv.set_window_size(1920, 1080)
    drv.base_url = "https://qauto2.forstudy.space"

    yield drv

    drv.quit()


def test_guest_flow(driver):
    home_page = HomePage(driver).open()
    home_page.click_guest_login_button()

    garage_page = GaragePage(driver)
    garage_page.wait_until_expenses_present(timeout_seconds=5)

    fuel_expenses = garage_page.get_fuel_expenses_button()
    instructions = garage_page.get_instructions_button()
    garage = garage_page.get_garage_button()


    assert fuel_expenses.is_displayed()
    assert instructions.is_displayed()
    assert garage.is_displayed()

    assert fuel_expenses.text.strip() == "Fuel expenses"
    assert instructions.text.strip() == "Instructions"
    assert garage.text.strip() == "Garage"
    time.sleep(1)

def test_login_form(driver):
    home_page = HomePage(driver).open()
    home_page.click_sign_in_button_by_complex_css()

    login_form = LoginForm(driver)
    time.sleep(1)

