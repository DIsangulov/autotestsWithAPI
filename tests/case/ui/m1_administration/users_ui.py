import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._1_Administration.adm_users_page import UsersPage


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
