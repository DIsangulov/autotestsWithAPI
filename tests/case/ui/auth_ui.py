import allure
from playwright.sync_api import expect, Page
from typing import TypedDict

from pages.Helpers.base_page import BasePage
from pages.UI.Auth.auth_page import AuthPage

RegistrationData = TypedDict('RegistrationData', {
    "rusname":      str,
    "username":     str,
    "password":     str,
    "email":        str,
    "mobile":       str,
    "department":   str,
    "title":        str,
    # "local": bool
})


@allure.step("Авторизация valid")
def valid_auth(browser: Page, auth_data: dict):
    page = AuthPage(browser)
    if page.check_auth():
        page.logout()

    with allure.step("Перейти на страницу Авторизации"):
        page.open()
        current_url = browser.url
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
        expect(page.HEADER_LOGO).to_be_visible(timeout=10000)


@allure.step("Авторизация invalid")
def invalid_auth(browser: Page, auth_data: dict):
    page = AuthPage(browser)
    if page.check_auth():
        page.logout()

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

    with allure.step("Авторизация не прошла"):
        expect(page.WRONG_LOGPASS_ALERT).to_be_visible()
        expect(page.HEADER_LOGO).to_be_visible(visible=False)


def valid_registration(browser: Page, registration_data):
    registration_data: RegistrationData

    page = AuthPage(browser)
    if page.check_auth():
        page.logout()

    with allure.step("Перейти на страницу Авторизации"):
        page.open()
        current_url = browser.url
        assert current_url.startswith(page.host + AuthPage.page_path), f"Страница авторизации не открылась"

    with allure.step("Клик на ссылку 'Регистрация'"):
        page.REGISTER_LINK.click()

    with allure.step("Открыто Модальное окно 'Регистрация'"):
        expect(page.registration.MODAL_CARD).to_be_visible()

    with allure.step("Ввести значение в поле 'Имя и фамилия'"):
        page.registration.INPUT_RUSNAME.fill(registration_data.get("rusname"))

    with allure.step("Ввести значение в поле 'Логин'"):
        page.registration.INPUT_USERNAME.fill(registration_data.get("username"))

    with allure.step("Ввести значение в поле 'Пароль'"):
        page.registration.INPUT_PASSWORD.fill(registration_data.get("password"))

    with allure.step("Ввести значение в поле 'Почта'"):
        page.registration.INPUT_EMAIL.fill(registration_data.get("email"))

    with allure.step("Ввести значение в поле 'Телефон'"):
        page.registration.INPUT_MOBILE.fill(registration_data.get("mobile"))

    with allure.step("Ввести значение в поле 'Отдел'"):
        page.registration.INPUT_DEPARTMENT.fill(registration_data.get("department"))

    with allure.step("Ввести значение в поле 'Должность'"):
        page.registration.INPUT_TITLE.fill(registration_data.get("title"))

    with allure.step("Кнопка 'Зарегистрировать' активна"):
        expect(page.registration.BUTTON_REGISTRATION).to_be_enabled()

    with allure.step("Клик по кнопке 'Зарегистрировать'"):
        page.registration.BUTTON_REGISTRATION.click()

    with allure.step("Модальное окно 'Регистрация' закрыто"):
        expect(page.registration.MODAL_CARD).not_to_be_visible()


def log_out(browser: Page):

    page = BasePage(browser)

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
        current_url = browser.url
        assert current_url.startswith(page.host + AuthPage.page_path), f"Страница авторизации не открылась"

# todo: hint: поле обязательно для заполнения логин и пароль
