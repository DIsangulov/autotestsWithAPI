import pytest
from playwright.sync_api import sync_playwright

from pages.Helpers.base_page import BasePage
from resourses.credentials import TestUsers

HOST = "https://10.130.0.22"    # todo: os.environ
# _auth_user    # todo: os.environ

# def _br(*, auth_data: dict = TestUsers.DpQaa, with_auth: bool = True, headless: bool = True):


@pytest.fixture(scope='class')
def browser_without_auth():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=True)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=True)
        # browser = playwright.chromium.launch(channel="chrome", headless=False)
        context = browser.new_context(
            ignore_https_errors=True,
            extra_http_headers={"user-agent": "Super-test-machine-v30801"}
        )
        page = context.new_page()
        BasePage(page, HOST).auth(auth_data=TestUsers.DpQaaLocal)
        yield page
        context.close()
        browser.close()


