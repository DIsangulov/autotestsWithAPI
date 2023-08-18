import pytest
from playwright.sync_api import sync_playwright
from pages.Helpers.base_page import BasePage


@pytest.fixture(scope='function')
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
        context = browser.new_context(
            ignore_https_errors=True,
            extra_http_headers={"user-agent": "Super-test-machine-v30818"}
        )
        page = context.new_page()
        BasePage(page).auth()
        yield page
        context.close()
        browser.close()
