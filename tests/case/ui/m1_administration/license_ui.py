import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._1_Administration.adm_licenses_page import LicensesPage


@allure.step("Открыть страницу Лицензии")
def open_page_by_steps(browser: Page):
    page = LicensesPage(browser)

    # шаг нужен, чтобы боковое меню было закрыто
    with allure.step("Перейти в 'Настройка уведомлений'"):
        page.goto_page("/notification-center")
        browser.wait_for_url(page.host + "/notification-center")

    with allure.step("Клик в боковом меню 'Администрирование'"):
        page.SB_ADMINISTRATION.click()

    with allure.step("Клик в меню 'Лицензии'"):
        page.SB_ADM_LICENSE.click()

    with allure.step("Открылась страница 'Лицензии'"):
        browser.wait_for_url(page.host + LicensesPage.page_path)
