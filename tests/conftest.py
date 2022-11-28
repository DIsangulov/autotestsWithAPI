import pytest
from seleniumwire import webdriver


@pytest.fixture(scope='class')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--kiosk")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def browser_for_cases():
    options = webdriver.ChromeOptions()
    options.add_argument("--kiosk")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()