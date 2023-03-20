from behave import fixture
from seleniumwire import webdriver

import behave


def before_scenario(context, browser):
    context.browser = webdriver.Chrome(executable_path='chromedriver')


def after_scenario(context, browser):
    context.browser.quit()

# @fixture
# def browser_chrome():
#     options = webdriver.ChromeOptions()
#
#     options.add_argument('--window-size=1920,1080')
#     options.add_argument("--headless")
#     options.add_argument('--no-sandbox')
#     options.add_argument('--disable-gpu')
#     options.add_argument('--disable-dev-shm-usage')
#
#     browser = webdriver.Chrome(executable_path='chromedriver', options=options)
#
#     yield browser
#     browser.quit()
