import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._1_Administration.adm_settings_page import AdmSettingsPage


class AdmSettingsCase(BaseCase):

    @allure.step("Открыть страницу Настройки")
    def open_page_by_steps(self):
        page = AdmSettingsPage(self._page)

        # шаг нужен, чтобы боковое меню было закрыто
        with allure.step("Перейти в 'Настройка уведомлений'"):
            page.goto_page("/notification-center")
            page.page.wait_for_url(page.host + "/notification-center")

        with allure.step("Клик в боковом меню 'Администрирование'"):
            page.SB_ADMINISTRATION.click()

        with allure.step("Клик в меню 'Настройки'"):
            page.SB_ADM_SETTINGS.click()

        with allure.step("Открылась страница 'Настройки'"):
            page.page.wait_for_url(page.host + AdmSettingsPage.page_path)
