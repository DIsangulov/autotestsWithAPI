import time

import allure

from pages.UI._0_Auth.auth_page import AuthPage


@allure.feature("UI - Страница авторизации")
class TestAuth:
    @allure.story("Авторизация")
    def test_valid_auth(self, browser):
        link = "https://10.130.0.22"
        page = AuthPage(browser, link)
        page.open()
