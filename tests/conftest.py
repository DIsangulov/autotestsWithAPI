import pytest
from playwright.sync_api import Playwright, sync_playwright


@pytest.fixture(scope='class')
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=False)
        # browser = playwright.chromium.launch(channel="chrome", headless=True)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        yield page
        page.close()
        browser.close()
