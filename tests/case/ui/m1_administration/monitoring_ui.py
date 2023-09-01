import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._1_Administration.adm_monitoring_page import MonitoringPage


class MonitoringCase(BaseCase):

    @allure.step("Открыть страницу Мониторинг")
    def open_page_by_steps(self):
        page = MonitoringPage(self._page)

        # шаг нужен, чтобы боковое меню было закрыто
        with allure.step("Перейти в 'Настройка уведомлений'"):
            page.goto_page("/notification-center")
            page.page.wait_for_url(page.host + "/notification-center")

        with allure.step("Клик в боковом меню 'Администрирование'"):
            page.SB_ADMINISTRATION.click()

        with allure.step("Клик в меню 'Мониторинг'"):
            page.SB_ADM_MONITORING.click()

        with allure.step("Открылась страница 'Мониторинг'"):
            page.page.wait_for_url(page.host + MonitoringPage.page_path)
