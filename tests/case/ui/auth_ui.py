import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._0_Auth.auth_page import AuthPage
from resourses.locators import MainLocators


class AuthCase(BaseCase):

    @allure.step("Авторизация valid")
    def valid_auth(self, auth_data: dict):
        page = AuthPage(self._page)

        with allure.step("Перейти на страницу Авторизации"):
            page.open()
            current_url = page.page.url
            assert current_url.startswith(page.host + AuthPage.page_path), f"Страница авторизации не открылась"

        with allure.step("Ввести логин и пароль"):
            page.LOGIN_INPUT.fill(auth_data.get("username"))
            page.PASSWORD_INPUT.fill(auth_data.get("password"))
            page.PASSWORD_VISIBLE.click()

        if auth_data.get("local"):
            with allure.step("Выбрать чекбокс 'локально'"):
                page.CHECKBOX_LOCAL.click()

        with allure.step('Нажать кнопку, "Войти"'):
            page.ENTER_BUTTON.click()
            logo = self._page.locator(MainLocators.HEADER_LOGO)

        with allure.step("Авторизация прошла"):
            expect(logo).to_be_visible(timeout=10000)

        # todo: hint: поле обязательно для заполнения логин
        # todo: hint: поле обязательно для заполнения пароль
