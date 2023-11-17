import allure
from playwright.sync_api import expect, Page
from typing import TypedDict

from pages.UI._1_Administration.adm_users_page import UsersPage

DomainUserRegistrationData = TypedDict('DomainUserRegistrationData', {
    "username":     str,
    "role_name":    str,
    "is_admin":     bool,
    "is_system":    bool,
    "is_tech":      bool
})

LocalUserRegistrationData = TypedDict('LocalUserRegistrationData', {
    "rusname":      str,
    "username":     str,
    "password":     str,
    "email":        str,
    "mobile":       str,
    "department":   str,
    "title":        str,
    # "local": bool
})


def transform_username_to_domain_name(username: str) -> str:
    # TODO: доменное имя меняется при наличии "/ или @"
    #  добавить логики при "/" или "@"
    domain_name = username + "@ngrsoftlab.ru"
    return domain_name.lower()


@allure.step("Открыть страницу Пользователи")
def open_page_by_steps(browser: Page):
    page = UsersPage(browser)

    # шаг нужен, чтобы боковое меню было закрыто
    with allure.step("Перейти в 'Настройка уведомлений'"):
        page.goto_page("/notification-center")
        browser.wait_for_url(page.host + "/notification-center")

    with allure.step("Клик в боковом меню 'Администрирование'"):
        page.SB_ADMINISTRATION.click()

    with allure.step("Клик в меню 'Пользователи'"):
        page.SB_ADM_USERS.click()

    with allure.step("Открылась страница 'Пользователи'"):
        browser.wait_for_url(page.host + UsersPage.page_path)


@allure.step("Добавить Доменного пользователя")
def add_domain_user(browser: Page, registration_data):
    registration_data: DomainUserRegistrationData

    page = UsersPage(browser)

    with allure.step("Открыть страницу 'Пользователи'"):
        page.open()
        expect(page.page).to_have_url(page.host + UsersPage.page_path)

    with allure.step("Клик по кнопке 'Добавить вручную'"):
        page.TOOLBAR_ADD_USER.click()

    with allure.step("Открыто модальное окно"):
        expect(page.add_user.MODAL_CARD).to_be_visible()

    with allure.step("В Модальном Окне: Открыта секция 'Доменный'"):
        expect(page.add_user.DOMAIN_SECTION).to_be_visible()

    with allure.step("Ввести значение 'Логин'"):
        page.add_user.INPUT_USERNAME_DOMAIN.fill(registration_data.get("username"))

    with allure.step("Выбрать роль в выпадающем списке"):
        page.select_role(registration_data.get("role_name"))

    if registration_data.get("is_admin"):
        with allure.step("Выбрать чекбокс 'Администратор'"):
            page.add_user.CHECKBOX_ADMIN.click()

    if registration_data.get("is_system"):
        with allure.step("Выбрать чекбокс 'Системная учетка'"):
            page.add_user.CHECKBOX_SYSTEM_USER.click()

    if registration_data.get("is_tech"):
        with allure.step("Выбрать чекбокс 'Технологическая учетка'"):
            page.add_user.CHECKBOX_TECH_USER.click()

    with allure.step("Кнопка 'Добавить' активна"):
        expect(page.add_user.BUTTON_ADD_DOMAIN).to_be_enabled()

    with allure.step("Клик по кнопке 'Добавить'"):
        page.add_user.BUTTON_ADD_DOMAIN.click()

    with allure.step("Модальное окно закрыто"):
        expect(page.add_user.MODAL_CARD).not_to_be_visible()

    with allure.step("Новый пользователь отображается на текущей странице"):
        expected_name = transform_username_to_domain_name(registration_data.get("username"))
        assert page.check_user_at_current_page(expected_name, timeout=600), \
            f"Новый пользователь не отображается на текущей странице\nexpected_name: {expected_name}"


@allure.step("Добавить Локального пользователя")
def add_local_user(browser: Page, registration_data):
    registration_data: LocalUserRegistrationData

    page = UsersPage(browser)

    with allure.step("Открыть страницу 'Пользователи'"):
        page.open()
        expect(page.page).to_have_url(page.host + UsersPage.page_path)

    with allure.step("Клик по кнопке 'Добавить вручную'"):
        page.TOOLBAR_ADD_USER.click()

    with allure.step("Открыто модальное окно"):
        expect(page.add_user.MODAL_CARD).to_be_visible()

    with allure.step("В Модальном Окне: Открыта секция 'Доменный'"):
        expect(page.add_user.DOMAIN_SECTION).to_be_visible()

    with allure.step("Клик по табу 'Локальный'"):
        page.add_user.TAB_LOCAL.click()

    with allure.step("В Модальном Окне: Открыта секция 'Локальный'"):
        expect(page.add_user.LOCAL_SECTION).to_be_visible()

    with allure.step("Заполнить поле 'Имя, Фамилия'"):
        page.add_user.INPUT_RUSNAME.fill(registration_data.get("rusname"))

    with allure.step("Заполнить поле 'Логин'"):
        page.add_user.INPUT_USERNAME.fill(registration_data.get("username"))

    with allure.step("Заполнить поле 'Пароль'"):
        page.add_user.INPUT_PASSWORD.fill(registration_data.get("password"))

    with allure.step("Заполнить поле 'Почта'"):
        page.add_user.INPUT_EMAIL.fill(registration_data.get("email"))

    with allure.step("Заполнить поле 'Телефон'"):
        page.add_user.INPUT_MOBILE.fill(registration_data.get("mobile"))

    with allure.step("Заполнить поле 'Отдел'"):
        page.add_user.INPUT_DEPARTMENT.fill(registration_data.get("department"))

    with allure.step("Заполнить поле 'Должность'"):
        page.add_user.INPUT_TITLE.fill(registration_data.get("title"))

    with allure.step("Кнопка 'Добавить' активна"):
        expect(page.add_user.BUTTON_ADD_LOCAL).to_be_enabled()

    with allure.step("Клик по кнопке 'Добавить'"):
        page.add_user.BUTTON_ADD_LOCAL.click()

    with allure.step("Модальное окно закрыто"):
        expect(page.add_user.MODAL_CARD).not_to_be_visible()

    with allure.step("Новый пользователь отображается на текущей странице"):
        expected_name = registration_data.get("username")
        assert page.check_user_at_current_page(expected_name), \
            f"Новый пользователь не отображается на текущей странице\nexpected_name: {expected_name}"
