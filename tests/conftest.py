import pytest
from selene import browser
from selenium import webdriver


BASE_URL = 'https://demowebshop.tricentis.com/'
LOGIN = "example1200@example.com"
PASSWORD = "123456"


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.open(BASE_URL)

    yield

    browser.quit()
