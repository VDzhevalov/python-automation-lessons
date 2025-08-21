import pytest
from lesson_28.forms.login_form import LoginForm
from lesson_28.pages.garage_page import GaragePage
from lesson_28.pages.home_page import HomePage
import time

@pytest.mark.parametrize("login, password", [
    ("123_aa@test.com", "12345678aA")])
def test_successful_login_form(driver, login, password):
    home_page = HomePage(driver).open()
    home_page.click_sign_in_button()

    login_form = LoginForm(driver)
    login_form.get_password_input_field().send_keys(password)
    login_form.get_email_input_field().send_keys(login)
    login_form.get_login_button().click()

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


