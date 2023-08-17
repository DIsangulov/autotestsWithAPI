import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._3_Analytics.reports_page import ReportsPage


class ReportsCase(BaseCase):

    @allure.step("Открыть страницу 'Отчеты'")
    def open_page_by_steps(self):
        page = ReportsPage(self._page)

        with allure.step("Перейти в 'Настройки уведомлений'"):
            page.goto_page("/notification-center")
            page.page.wait_for_url(page.host + "/notification-center")

        with allure.step("Клик в боковом меню 'Аналитика'"):
            page.SB_ANALYTICS.click()

        with allure.step("Клик в меню 'Отчеты'"):
            page.SB_ANALYTICS_REPORTS.click()

        with allure.step("Открылась страница 'Отчеты'"):
            page.page.wait_for_url(page.host + ReportsPage.page_path)
