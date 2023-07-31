import time

import pytest
from playwright.sync_api import sync_playwright

# def _br(*, auth_data: dict = TestUsers.DpQaa, with_auth: bool = True, headless: bool = True):


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=True)
        # browser = playwright.chromium.launch(channel="chrome", headless=False)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        yield page
        context.close()
        browser.close()


# @pytest.fixture(scope='class')
# def browser_headed():
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(channel="chrome", headless=False)
#         context = browser.new_context(ignore_https_errors=True)
#         page = context.new_page()
#         yield page
#         context.close()
#         browser.close()
