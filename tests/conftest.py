import pytest
from playwright.sync_api import sync_playwright
from pages.Helpers.base_page import BasePage

browser_headless = True
default_timeout = 10000
default_viewport = {'width': 1920, 'height': 1080}


@pytest.fixture(scope='function')
def browser_without_auth():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=browser_headless)
        context = browser.new_context(ignore_https_errors=True, viewport=default_viewport)
        page = context.new_page()
        page.set_default_timeout(default_timeout)
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=browser_headless)
        context = browser.new_context(
            ignore_https_errors=True,
            viewport=default_viewport,
            extra_http_headers={"user-agent": "Super-test-machine-v31010"}
        )
        page = context.new_page()
        page.set_default_timeout(default_timeout)
        # BasePage(page).auth()
        yield page
        context.close()
        browser.close()
