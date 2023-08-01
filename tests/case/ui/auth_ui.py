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

        with allure.step("Кнопка 'Войти' неактивна"):
            expect(page.ENTER_BUTTON).to_be_disabled()

        with allure.step("Ввести значение в поле 'Логин'"):
            page.LOGIN_INPUT.fill(auth_data.get("username"))

        with allure.step("Ввести значение в поле 'Пароль'"):
            page.PASSWORD_INPUT.fill(auth_data.get("password"))

        with allure.step("Кнопка 'Войти' активна"):
            expect(page.ENTER_BUTTON).to_be_enabled()

        with allure.step("Пароль скрыт символами *"):
            expect(page.PASSWORD_INPUT).to_have_attribute(name="type", value="password")

        with allure.step("Раскрытие пароля, нажать значок 'Глаз'"):
            page.PASSWORD_VISIBLE.click()

        with allure.step("Пароль 'раскрыт'"):
            expect(page.PASSWORD_INPUT).to_have_attribute(name="type", value="text")

        if auth_data.get("local"):
            with allure.step("Выбрать чекбокс 'локально'"):
                page.CHECKBOX_LOCAL.click()

        with allure.step('Кликнуть по кнопке "Войти"'):
            page.ENTER_BUTTON.click()
            logo = self._page.locator(MainLocators.HEADER_LOGO)

        with allure.step("Авторизация прошла"):
            expect(logo).to_be_visible(timeout=10000)

    @allure.step("Авторизация invalid")
    def invalid_auth(self, auth_data: dict):
        page = AuthPage(self._page)

        with allure.step("Перейти на страницу Авторизации"):
            page.open()
            current_url = page.page.url
            assert current_url.startswith(page.host + AuthPage.page_path), f"Страница авторизации не открылась"

        # tit 427
        with allure.step("Кнопка 'Войти' неактивна"):
            expect(page.ENTER_BUTTON).to_be_disabled()

        with allure.step("Ввести значение в поле 'Логин'"):
            page.LOGIN_INPUT.fill(auth_data.get("username"))

        with allure.step("Ввести значение в поле 'Пароль'"):
            page.PASSWORD_INPUT.fill(auth_data.get("password"))

        with allure.step("Кнопка 'Войти' активна"):
            expect(page.ENTER_BUTTON).to_be_enabled()

        with allure.step("Пароль скрыт символами *"):
            expect(page.PASSWORD_INPUT).to_have_attribute(name="type", value="password")

        with allure.step("Раскрытие пароля, нажать значок 'Глаз'"):
            page.PASSWORD_VISIBLE.click()

        with allure.step("Пароль 'раскрыт'"):
            expect(page.PASSWORD_INPUT).to_have_attribute(name="type", value="text")

        if auth_data.get("local"):
            with allure.step("Выбрать чекбокс 'локально'"):
                page.CHECKBOX_LOCAL.click()

        with allure.step('Кликнуть по кнопке "Войти"'):
            page.ENTER_BUTTON.click()
            logo = self._page.locator(MainLocators.HEADER_LOGO)

        with allure.step("Авторизация не прошла"):
            expect(page.WRONG_LOGPASS_ALERT).to_be_visible()
            expect(logo).to_be_visible(visible=False)

        # todo: hint: поле обязательно для заполнения логин
        # todo: hint: поле обязательно для заполнения пароль
