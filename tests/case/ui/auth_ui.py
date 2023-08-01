import time

import allure
from playwright.sync_api import expect

from pages.UI._0_Auth.auth_page import AuthPage
from resourses.credentials import TestUsers
from resourses.locators import MainLocators


class AuthCase:

    def __init__(self, browser, host):
        self.browser = browser
        self.host = host

    @allure.step("check1")
    def valid_auth(self):
        page = AuthPage(self.browser, self.host)

        with allure.step("Перейти на страницу Авторизации"):
            page.open()
            # todo: убедиться, что страница открылась

        with allure.step("Ввести логин и пароль"):
            page.LOGIN_INPUT_1.fill(TestUsers.DpQaa.get("username"))
            page.PASSWORD_INPUT_1.fill(TestUsers.DpQaa.get("password"))
            page.PASSWORD_VISIBLE_1.click()

        with allure.step('Нажать кнопку, "Войти"'):
            page.ENTER_BUTTON.click()
            logo = page.page.locator(MainLocators.HEADER_LOGO)

        with allure.step("Авторизация прошла"):
            expect(logo).to_be_visible(timeout=10000)

        # todo: hint: поле обязательно для заполнения логин
        # todo: hint: поле обязательно для заполнения пароль

    def fail(self):
        assert False, "Это фиаско"
