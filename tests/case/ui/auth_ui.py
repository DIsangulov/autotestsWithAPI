import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._0_Auth.auth_page import AuthPage
from resourses.locators import MainLocators


class AuthCase(BaseCase):

    @allure.step("Авторизация")
    def valid_auth_no_steps(self, auth_data: dict):
        page = AuthPage(self._page)
        page.open()
        current_url = page.page.url
        assert current_url.startswith(page.host + AuthPage.page_path), f"Страница авторизации не открылась"

        page.LOGIN_INPUT.fill(auth_data.get("username"))
        page.PASSWORD_INPUT.fill(auth_data.get("password"))
        if auth_data.get("local"):
            page.CHECKBOX_LOCAL.click()
        page.ENTER_BUTTON.click()
        logo = self._page.locator(MainLocators.HEADER_LOGO)
        expect(logo).to_be_visible(timeout=10000)

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

        with allure.step("Авторизация прошла"):
            logo = self._page.locator(MainLocators.HEADER_LOGO)
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

        with allure.step("Авторизация не прошла"):
            logo = self._page.locator(MainLocators.HEADER_LOGO)
            expect(page.WRONG_LOGPASS_ALERT).to_be_visible()
            expect(logo).to_be_visible(visible=False)

    def log_out(self, auth_data: dict):

        # step.авторизация
        self.valid_auth_no_steps(auth_data)

        page = AuthPage(self._page)

        with allure.step("Кликнуть на выпадающее меню 'Пользователь'"):
            page.PROFILE_BUTTON.click()

        # with allure.step("Отображается выпадающий список с кнопками"):
        #     # ngr-card display none

        with allure.step("- 'Профиль пользователя'"):
            expect(page.PB_USER_PROFILE).to_be_visible()

        with allure.step("- 'Настройки уведомлений'"):
            expect(page.PB_NOTIFICATION_SETTINGS).to_be_visible()

        with allure.step("- 'Выход'"):
            expect(page.PB_SIGN_OUT).to_be_visible()

        with allure.step("Кликнуть по кнопке 'Выйти'"):
            page.PB_SIGN_OUT.click()

        with allure.step("Отображается страница авторизации"):
            current_url = page.page.url
            assert current_url.startswith(page.host + AuthPage.page_path), f"Страница авторизации не открылась"

    # todo: hint: поле обязательно для заполнения логин
    # todo: hint: поле обязательно для заполнения пароль
