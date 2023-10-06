import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._1_Administration.adm_sessions_page import SessionsPage


@allure.step("Открыть страницу Сессии")
def open_page_by_steps(browser: Page):
    page = SessionsPage(browser)

    # шаг нужен, чтобы боковое меню было закрыто
    with allure.step("Перейти в 'Настройка уведомлений'"):
        page.goto_page("/notification-center")
        browser.wait_for_url(page.host + "/notification-center")

    with allure.step("Клик в боковом меню 'Администрирование'"):
        page.SB_ADMINISTRATION.click()

    with allure.step("Клик в меню 'Сессии'"):
        page.SB_ADM_SESSIONS.click()

    with allure.step("Открылась страница 'Сессии'"):
        browser.wait_for_url(page.host + SessionsPage.page_path)
