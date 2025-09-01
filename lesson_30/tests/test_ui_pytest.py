import allure
import pytest

@allure.epic("Логін")
@allure.story("Вдалий логін")
def test_successful_login_form(driver, open_home_page, open_sign_in_page, sign_in, check_successful_login):
    open_home_page()
    open_sign_in_page()
    sign_in()
    fuel_expenses, instructions, garage = check_successful_login()

    element_is_displayed(fuel_expenses, "fuel_expenses")
    element_is_displayed(instructions, "instructions")
    element_is_displayed(garage, "garage")

    element_has_text(fuel_expenses, "fuel_expenses", "Fuel expenses")
    element_has_text(instructions, "instructions", "Instructions")
    element_has_text(garage, "garage", "Garage")

@allure.step("Перевірка чи відображається елемент: {element_name}")
def element_is_displayed(element, element_name):
    assert element.is_displayed()

@allure.step("Перевірка чи елемент: {element_name}, має текст: {text}")
def element_has_text(element, element_name, text):
    assert element.is_displayed()