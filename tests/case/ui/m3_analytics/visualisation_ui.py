import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._3_Analytics.visualization_page import VisualisationPage


class VisualisationCase(BaseCase):

    @allure.step("Открыть страницу 'Визуализации'")
    def open_page_by_steps(self):
        page = VisualisationPage(self._page)

        with allure.step("Перейти в 'Настройки уведомлений'"):
            page.goto_page("/notification-center")
            page.page.wait_for_url(page.host + "/notification-center")

        with allure.step("Клик в боковом меню 'Аналитика'"):
            page.SB_ANALYTICS.click()

        with allure.step("Клик в меню 'Визуализации'"):
            page.SB_ANALYTICS_VISUALISATIONS.click()

        with allure.step("Открылась страница 'Визуализации'"):
            page.page.wait_for_url(page.host + VisualisationPage.page_path)
