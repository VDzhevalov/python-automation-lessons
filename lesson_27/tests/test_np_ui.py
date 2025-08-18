import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


from lesson_27.pages.nova_poshta_home_page import NPHomePage


@pytest.fixture(scope='session')
def driver():
    opts = Options()
    drv = webdriver.Chrome(options=opts)
    drv.set_window_size(1920, 1080)
    drv.base_url = "https://tracking.novaposhta.ua/"

    yield drv

    drv.quit()

def test_np_tracking(driver):
    home_page = NPHomePage(driver).open()
    home_page.get_track_num_input_field_by_id().send_keys("12345678900")
    home_page.get_submit_track_search_button().click()

    error_elem = home_page.get_error_message()
    error_text = error_elem.text.strip()

    assert "Ми не знайшли посилку за таким номером" in error_text