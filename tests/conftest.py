import os
import pytest
from playwright.sync_api import sync_playwright
from pages.Helpers.base_page import BasePage
from resourses.credentials import TestUsers

HOST = os.environ.get('TARGET_URL', "https://10.130.0.22")

default_user = {
    "username": os.environ.get('TARGET_UI_USER', TestUsers.DpQaaLocal.get("username")),
    "password": os.environ.get('TARGET_UI_PASSWORD', TestUsers.DpQaaLocal.get("password")),
    "local": os.environ.get('TARGET_UI_USER_IS_LOCAL', TestUsers.DpQaaLocal.get("local")),
}


@pytest.fixture(scope='function')
def browser_without_auth():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=True)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        BasePage.set_host(HOST)
        yield page
        context.close()
        browser.close()


@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome", headless=True)
        context = browser.new_context(
            ignore_https_errors=True,
            extra_http_headers={"user-agent": "Super-test-machine-v30801"}
        )
        page = context.new_page()
        BasePage.set_host(HOST)
        BasePage(page).auth(auth_data=default_user)
        yield page
        context.close()
        browser.close()
