import pytest
from seleniumwire import webdriver


@pytest.fixture(scope='class')
def browser():
    options = webdriver.ChromeOptions()
    # options.add_argument('--window-size=1920,1080')
    # options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--start-maximized')
    # browser = webdriver.Remote(command_executor="http://172.17.0.2:4444/wd/hub", options=options)
    # browser = webdriver.Chrome(executable_path='chromedriver', options=options)
    # options.binary_location = '/Applications/Yandex.app/Contents/MacOS/Yandex'
    options.binary_location = './Yandex'
    browser = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver')
    # browser = webdriver.Chrome(executable_path='yandexdriver', options=options)
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