import time

import pytest

from pages.UI._0_Auth.auth_page import AuthPage


class TestUsersDefinitionCrud:
    # def test_enter_as_user(self, browser):
    #     link = "https://10.130.0.22/"
    #     page = AuthPage(browser, link)
    #     page.open()
    #     page.enter_as_user()
    #     page.should_enter_be_successful()

    def test_visible_pass(self, browser):
        link = "https://10.130.0.22/"
        page = AuthPage(browser, link)
        page.open()
        page.visible_pass()
