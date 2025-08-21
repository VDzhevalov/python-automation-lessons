import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='session')
def driver():
    opts = Options()
    drv = webdriver.Chrome(options=opts)
    drv.set_window_size(1920, 1080)
    drv.base_url = "https://qauto2.forstudy.space"

    yield drv
    drv.quit()