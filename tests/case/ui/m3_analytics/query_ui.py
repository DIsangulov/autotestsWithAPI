import time

import allure
from playwright.sync_api import expect, Page

from pages.UI._3_Analytics.requests_page import QueriesPage


@allure.step("Открыть страницу 'Запросы'")
def open_page_by_steps(browser: Page):
    page = QueriesPage(browser)

    with allure.step("Перейти в 'Настройки уведомлений'"):
        page.goto_page("/notification-center")
        browser.wait_for_url(page.host + "/notification-center")

    with allure.step("Клик в боковом меню 'Аналитика'"):
        page.SB_ANALYTICS.click()

    with allure.step("Клик в меню 'Запросы'"):
        page.SB_ANALYTICS_QUERIES.click()

    with allure.step("Открылась страница 'Запросы'"):
        browser.wait_for_url(page.host + QueriesPage.page_path)
