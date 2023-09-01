import time

import allure
from playwright.sync_api import expect

from pages.Helpers.base_case import BaseCase
from pages.UI._1_Administration.adm_update_page import UpdatesPage, UpdatesAdditionsPage, UpdatesVersionsPage


class UpdatesCase(BaseCase):

    @allure.step("Открыть страницу Обновление")
    def open_page_by_steps(self):
        page = UpdatesPage(self._page)

        # шаг нужен, чтобы боковое меню было закрыто
        with allure.step("Перейти в 'Настройка уведомлений'"):
            page.goto_page("/notification-center")
            page.page.wait_for_url(page.host + "/notification-center")

        with allure.step("Клик в боковом меню 'Администрирование'"):
            page.SB_ADMINISTRATION.click()

        with allure.step("Клик в меню 'Обновление'"):
            page.SB_ADM_UPDATES.click()

        with allure.step("Открылась страница 'Обновление'"):
            page.page.wait_for_url(page.host + UpdatesVersionsPage.page_path)

        with allure.step("Клик по вкладке 'Дополнения'"):
            page.TAB_ADDITIONS.click()
        with allure.step("Открылась вкладка 'Дополнения'"):
            page.page.wait_for_url(page.host + UpdatesAdditionsPage.page_path)
        with allure.step("Клик по вкладке 'Версии компонентов'"):
            page.TAB_VERSIONS.click()
        with allure.step("Открылась вкладка 'Версии компонентов'"):
            page.page.wait_for_url(page.host + UpdatesVersionsPage.page_path)
