import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._4_xBA.xba_statistics_page import XbaStatisticsPage


class XbaStatisticsCase(BaseCase):

    @allure.step("Открыть страницу 'Статистика xBA'")
    def open_page_by_steps(self):
        page = XbaStatisticsPage(self._page)

        with allure.step("Перейти в 'Настройки уведомлений'"):
            page.goto_page("/notification-center")
            page.page.wait_for_url(page.host + "/notification-center")

        with allure.step("Клик в боковом меню 'xBA'"):
            page.SB_XBA.click()

        with allure.step("Клик в меню 'Статистика xBA'"):
            page.SB_XBA_STATISTICS.click()

        with allure.step("Открылась страница 'Статистика xBA'"):
            page.page.wait_for_url(page.host + XbaStatisticsPage.page_path)
