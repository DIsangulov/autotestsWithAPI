import pytest
from seleniumwire import webdriver


@pytest.fixture(scope='class')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    # options.add_argument("--headless")
    browser = webdriver.Remote(command_executor="http://172.18.0.2:5555/wd/hub", options=options)
    # browser = webdriver.Chrome(executable_path='chromedriver', options=options)
    # browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    yield browser
    browser.quit()


@pytest.fixture(scope='function')
def browser_for_cases():
    options = webdriver.ChromeOptions()
    options.add_argument("--kiosk")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()