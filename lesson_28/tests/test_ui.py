import pytest

def test_successful_login_form(driver, open_home_page, open_sign_in_page, sign_in, check_successful_login):
    open_home_page()
    open_sign_in_page()
    sign_in()
    fuel_expenses, instructions, garage = check_successful_login()

    assert fuel_expenses.is_displayed()
    assert instructions.is_displayed()
    assert garage.is_displayed()

    assert fuel_expenses.text.strip() == "Fuel expenses"
    assert instructions.text.strip() == "Instructions"
    assert garage.text.strip() == "Garage"


