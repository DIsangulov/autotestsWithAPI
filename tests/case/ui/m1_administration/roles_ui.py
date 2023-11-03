import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._1_Administration.adm_roles_page import RolesPage


@allure.step("Открыть страницу Роли")
def open_page_by_steps(browser: Page):
    page = RolesPage(browser)

    # шаг нужен, чтобы боковое меню было закрыто
    with allure.step("Перейти в 'Настройка уведомлений'"):
        page.goto_page("/notification-center")
        browser.wait_for_url(page.host + "/notification-center")

    with allure.step("Клик в боковом меню 'Администрирование'"):
        page.SB_ADMINISTRATION.click()

    with allure.step("Клик в меню 'Роли'"):
        page.SB_ADM_ROLES.click()

    with allure.step("Открылась страница 'Роли'"):
        browser.wait_for_url(page.host + RolesPage.page_path)
