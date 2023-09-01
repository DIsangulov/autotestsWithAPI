import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._3_Analytics.requests_page import QueriesPage


class QueriesCase(BaseCase):

    @allure.step("Открыть страницу 'Запросы'")
    def open_page_by_steps(self):
        page = QueriesPage(self._page)

        with allure.step("Перейти в 'Настройки уведомлений'"):
            page.goto_page("/notification-center")
            page.page.wait_for_url(page.host + "/notification-center")

        with allure.step("Клик в боковом меню 'Аналитика'"):
            page.SB_ANALYTICS.click()

        with allure.step("Клик в меню 'Запросы'"):
            page.SB_ANALYTICS_QUERIES.click()

        with allure.step("Открылась страница 'Запросы'"):
            page.page.wait_for_url(page.host + QueriesPage.page_path)
