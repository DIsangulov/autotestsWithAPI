import time

from pages.UI._0_Auth.auth_page import AuthPage


class TestAuth:
    def test_valid_auth(self, browser):
        link = "https://10.130.0.22"
        page = AuthPage(browser, link)
        page.open()
