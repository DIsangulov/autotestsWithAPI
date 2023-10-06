import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._1_Administration.adm_notification_list_page import AdmNotificationListPage


@allure.step("Открыть страницу Журнал Уведомлений")
def open_page_by_steps(browser: Page):
    page = AdmNotificationListPage(browser)

    # шаг нужен, чтобы боковое меню было закрыто
    with allure.step("Перейти в 'Настройка уведомлений'"):
        page.goto_page("/notification-center")
        browser.wait_for_url(page.host + "/notification-center")

    with allure.step("Клик в боковом меню 'Администрирование'"):
        page.SB_ADMINISTRATION.click()

    with allure.step("Клик в меню 'Журнал уведомлений'"):
        page.SB_ADM_NOTIFICATION_LIST.click()

    with allure.step("Открылась страница 'Журнал уведомлений'"):
        browser.wait_for_url(page.host + AdmNotificationListPage.page_path)
